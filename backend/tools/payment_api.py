from tools.mongodb_tool import db
from datetime import datetime

def add_payment(order_id: str, amount: float, date: str = None) -> str:
   
    if not order_id or not amount:
        return "order_id and amount are required."

    try:
        payment_date = datetime.fromisoformat(date) if date else datetime.utcnow()
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD or ISO format."

    payment = {
        "order_id": order_id,
        "amount": amount,
        "date": payment_date
    }

    result = db.payments.insert_one(payment)
    return f"Payment added with ID: {str(result.inserted_id)}"
