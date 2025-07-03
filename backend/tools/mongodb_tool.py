from tools.base_tool import BaseTool
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import os, json
from dotenv import load_dotenv
from pymongo.errors import ServerSelectionTimeoutError

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]

def is_mongo_connected() -> bool:
    try:
        # Trigger a lightweight command to confirm connection
        client.admin.command("ping")
        return True
    except ServerSelectionTimeoutError:
        return False
def clean(doc):
    def _convert(v):
        if isinstance(v, ObjectId): return str(v)
        if isinstance(v, datetime): return v.isoformat()
        if isinstance(v, list): return [_convert(i) for i in v]
        if isinstance(v, dict): return {k: _convert(vv) for k, vv in v.items()}
        return v
    return {k: _convert(v) for k, v in doc.items()}

class MongoDBTool(BaseTool):
    name = "MongoDBTool"
    description = "Read data from clients, orders, payments, courses, classes"

    def _run(self, query: str) -> str:
        q = query.lower()
        # upcoming classes
        if "classes" in q or "available" in q:
            docs = db.classes.find({"status": "scheduled", "start_time": {"$gte": datetime.utcnow()}})
            return json.dumps([clean(d) for d in docs])
        if "payment" in q and "#" in q:
            oid = q.split("#")[1].split()[0]
            docs = db.payments.find({"order_id": oid})
            return json.dumps([clean(d) for d in docs])
        # order info
        if "order" in q and "#" in q:
            oid = q.split("#")[1].split()[0]
            doc = db.orders.find_one({"order_id": oid})
            return json.dumps(clean(doc)) if doc else f"Order {oid} not found."
        # payments for order
       
        # client lookup
        for field in ("name", "email", "phone"):
            if field in q:
                val = q.split(field)[1].strip().strip(": ").strip()
                doc = db.clients.find_one({field: {"$regex": val, "$options": "i"}})
                return json.dumps(clean(doc)) if doc else f"Client not found by {field}='{val}'."
        return "No matching MongoDB action."
