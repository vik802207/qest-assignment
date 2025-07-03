from tools.base_tool import BaseTool
from tools.mongodb_tool import db
import re

class ExternalAPI(BaseTool):
    name = "ExternalAPI"
    description = "Create new orders or clients"

    def _run(self, query: str) -> str:
        q = query.lower()
        # Create order: "create order for <service> for client <Name>"
        m = re.search(r"order for ([\w ]+?) for client ([\w ]+)", q)
        if m:
            service = m.group(1).strip().title()
            client_name = m.group(2).strip().title()
            client = db.clients.find_one({"name": {"$regex": client_name, "$options": "i"}})
            if not client:
                return f"Client '{client_name}' not found."
            order = {
                "order_id": str(db.orders.estimated_document_count() + 1),
                "client_id": client["_id"],
                "service": service,
                "amount": 1000,
                "status": "pending"
            }
            res = db.orders.insert_one(order)
            return f"Order created: {service} for {client_name}, ID={str(res.inserted_id)}"
        return "Unsupported external action."
