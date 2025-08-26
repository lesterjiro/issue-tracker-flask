# Issue Tracker - Cloud-Native Architecture

A production-style **cloud issue tracker** built to demonstrate end-to-end cloud engineering skills.
This project shows how to design, deploy, and integrate multiple AWS services into a working system.

## Why This Project Matters

Modern engineering teams need systems that are:

* **Reliable** → RDS for transactional data, DynamoDB for audit logs
* **Observable** → CloudWatch logging and metrics
* **Scalable** → Deployed inside a secure Amazon VPC on EC2
* **Data-driven** → Matplotlib visualizations for operational insights

This project demonstrates the ability to architect, build, and operate such a system from scratch.

## Architecture Overview

* **Amazon VPC** → Isolated, secure networking
* **Amazon EC2** → Hosts Flask web + API app
* **Amazon RDS (MySQL)** → Stores persistent issue data
* **Amazon DynamoDB** → Immutable action logs for traceability
* **Amazon CloudWatch** → Request/response logging, system monitoring
* **Matplotlib** → Visual dashboards (e.g., issues by status)

## Core Features

✔️ Add, update, and view issues via **REST API** and simple HTML forms
✔️ **Immutable audit logs** in DynamoDB for every status change
✔️ **CloudWatch integration** to centralize logs for debugging + monitoring
✔️ **Data visualization** with Matplotlib, embedded in the Flask UI
✔️ **End-to-end AWS networking** inside a custom VPC


## Skills Demonstrated

* Infrastructure provisioning on AWS (VPC, EC2, RDS, IAM, DynamoDB)
* Secure database design and API integration
* Logging and observability with CloudWatch
* Python (Flask, boto3, Matplotlib)
* GitHub project setup with requirements.txt and documentation


## Quick Start

```bash
git clone https://github.com/lesterjiro/issue-tracker-flask.git
cd issue-tracker-flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

