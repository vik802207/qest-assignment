# 📁 tools/add_entity.py
from tools.mongodb_tool import db
from datetime import datetime


def add_client(data: dict):
    if not data.get("name") or not data.get("email"):
        return "Client name and email are required."
    result = db.clients.insert_one(data)
    return f"Client added with ID: {str(result.inserted_id)}"


def add_order(data: dict):
    if not data.get("client_id") or not data.get("service"):
        return "Order must have client_id and service."
    data["status"] = data.get("status", "pending")
    data["amount"] = float(data.get("amount", 0))
    result = db.orders.insert_one(data)
    return f"Order added with ID: {str(result.inserted_id)}"


def add_payment(data: dict):
    if not data.get("order_id") or not data.get("amount"):
        return "Payment must have order_id and amount."
    data["amount"] = float(data["amount"])
    data["date"] = datetime.fromisoformat(data.get("date")) if data.get("date") else datetime.utcnow()
    result = db.payments.insert_one(data)
    return f"Payment added with ID: {str(result.inserted_id)}"


def add_course(data: dict):
    if not data.get("title"):
        return "Course title is required."
    result = db.courses.insert_one(data)
    return f"Course added with ID: {str(result.inserted_id)}"


def add_class(data: dict):
    if not data.get("course_id") or not data.get("instructor"):
        return "Class must have course_id and instructor."
    data["date"] = datetime.fromisoformat(data.get("date")) if data.get("date") else datetime.utcnow()
    result = db.classes.insert_one(data)
    return f"Class added with ID: {str(result.inserted_id)}"
