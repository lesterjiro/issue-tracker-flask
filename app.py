from flask import Flask, request, jsonify, request, send_file, render_template
from logger import logger
from db import query_all, execute
from logs import log_action
from charts import generate_issue_chart

app = Flask(__name__)

@app.before_request
def log_request():
    logger.info("Incoming request: %s %s from %s",
                request.method, request.path, request.remote_addr)

@app.after_request
def log_response(response):
    logger.info("Response: %s %s → %s",
                request.method, request.path, response.status)
    return response

@app.get("/form/add")
def add_form():
    return render_template("add_form.html")

@app.get("/form/update/<int:issue_id>")
def update_form(issue_id):
    return render_template("update_form.html", issue_id=issue_id)

@app.get("/")
def home():
    logger.info("Health check hit: /")
    return "Issue Tracker is running. Try /issues"

@app.get("/chart")
def chart_view():
    chart_type = request.args.get("type", "bar")  # default = bar
    if chart_type not in ("bar", "pie"):
        return {"error": "Invalid chart type. Use ?type=bar or ?type=pie"}, 400

    path = generate_issue_chart(chart_type)
    return send_file(path, mimetype="image/png")

@app.get("/chart")
def chart():
    chart_type = request.args.get("type", "bar")  # default = bar
    if chart_type not in ("bar", "pie"):
        logger.warning("Chart request with invalid type=%s", chart_type)
        return {"error": "Invalid chart type. Use ?type=bar or ?type=pie"}, 400

    path = generate_issue_chart(chart_type)
    logger.info("Generated chart: type=%s → %s", chart_type, path)
    return send_file(path, mimetype="image/png")


@app.get("/issues")
def list_issues():
    rows = query_all("""
        SELECT issue_id, title, description, status, assigned_to, created_at
        FROM Issues
        ORDER BY created_at DESC
    """)
    return jsonify(rows), 200

@app.post("/add")
def add_issue():
    data = request.get_json(silent=True) or request.form 
    title = (data.get("title") or "").strip()
    description = (data.get("description") or "").strip()
    assigned_to = (data.get("assigned_to") or "").strip()
    status = (data.get("status") or "Open").strip()  # default Open

    if not title:
        return {"error": "title is required"}, 400

    sql = """
        INSERT INTO Issues (title, description, status, assigned_to)
        VALUES (%s, %s, %s, %s)
    """
    last_id, _ = execute(sql, (title, description, status, assigned_to or None))
    logger.info("Added issue %s: %s (assigned_to=%s, status=%s)",
                last_id, title, assigned_to, status)

    log_action(str(last_id), f"Issue created with status {status}")
    return {"created_id": last_id}, 201


@app.route("/update/<int:issue_id>", methods=["PUT", "POST"])
def update_issue(issue_id):
    data = request.get_json(silent=True) or request.form
    status = (data.get("status") or "").strip()
    if not status:
        logger.warning("Update attempt without status for issue_id=%s", issue_id)
        return {"error": "status is required"}, 400

    _, affected = execute("UPDATE Issues SET status=%s WHERE issue_id=%s", (status, issue_id))

    if affected == 0:
        rows = query_all("SELECT status FROM Issues WHERE issue_id=%s", (issue_id,))
        if not rows:
            logger.warning("Update failed: issue_id=%s not found", issue_id)
            return {"error": f"issue_id {issue_id} not found"}, 404

        current_status = rows[0]["status"]
        logger.info("No update: issue_id=%s already has status=%s", issue_id, current_status)
        return {"message": f"issue_id {issue_id} already has status {current_status}"}, 200

    logger.info("Updated issue_id=%s to status=%s", issue_id, status)
    log_action(str(issue_id), f"Status updated to {status}")

    return {"updated_id": issue_id, "new_status": status}, 200



if __name__ == "__main__":
    # Dev run; use 0.0.0.0 so you can tunnel in 
    app.run(host="0.0.0.0", port=5000)
