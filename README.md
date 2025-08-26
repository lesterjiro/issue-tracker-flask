# Issue Tracker - Cloud Architecture

A production-inspired issue tracking system built with **Flask** and **AWS services**, designed to demonstrate full-stack cloud engineering skills.

## Architecture

* **Flask (EC2)** → Application layer with REST API and simple HTML forms
* **Amazon RDS (MySQL)** → Persistent storage for issues
* **Amazon DynamoDB** → Immutable action logs for updates
* **Amazon CloudWatch** → Centralized application + audit logging
* **Matplotlib** → Operational charts (issues by status, trends)

This setup simulates a **real-world microservice architecture** using managed AWS services.

## Features

* Create, update, and list issues via API and HTML forms
* Durable relational storage (RDS) + append-only logs (DynamoDB)
* Cloud-native observability with CloudWatch integration
* Visual reporting of issue status using Python charts

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/lesterjiro/issue-tracker-flask.git
cd issue-tracker-flask

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
```

## Example Endpoints

* `GET /issues` → List all issues
* `POST /add` → Add a new issue
* `PUT /update/<id>` → Update issue status


## Why This Project?

This project demonstrates:

* Building a **scalable backend** with Flask and AWS RDS
* Designing **audit-friendly architectures** with DynamoDB logs
* Leveraging **CloudWatch observability** for production readiness
* Showcasing **data visualization** with Python

Ideal for cloud engineers and backend developers looking to highlight **real-world cloud integration skills**.

