import os
import matplotlib.pyplot as plt
from db import query_all

def generate_issue_chart(chart_type="bar"):
    # Query counts by status
    rows = query_all("SELECT status, COUNT(*) as count FROM Issues GROUP BY status")

    statuses = [row["status"] for row in rows]
    counts = [row["count"] for row in rows]

    plt.figure(figsize=(6, 4))

    if chart_type == "pie":
        plt.pie(counts, labels=statuses, autopct="%1.1f%%", startangle=90)
        plt.title("Issues by Status (Pie)")
    else:
        plt.bar(statuses, counts, color="skyblue")
        plt.title("Issues by Status (Bar)")
        plt.xlabel("Status")
        plt.ylabel("Count")

    plt.tight_layout()
    os.makedirs("static", exist_ok=True)
    path = f"static/issues_{chart_type}.png"
    plt.savefig(path)
    plt.close()
    return path
