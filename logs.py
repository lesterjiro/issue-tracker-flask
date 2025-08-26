import boto3
import uuid
from datetime import datetime

# DynamoDB client
dynamodb = boto3.resource("dynamodb", region_name="ap-southeast-1")  # adjust region if needed
logs_table = dynamodb.Table("IssueLogs")

def log_action(issue_id: str, action: str):
    """Insert a log into DynamoDB IssueLogs table."""
    log_item = {
        "log_id": str(uuid.uuid4()),
        "issue_id": str(issue_id),
        "action": action,
        "timestamp": datetime.utcnow().isoformat()
    }
    logs_table.put_item(Item=log_item)
    return log_item
