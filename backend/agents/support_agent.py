# agents/support_agent.py

from tools.mongodb_tool import MongoDBTool
from tools.external_api_tool import ExternalAPI

class SupportAgent:
    """
    A simple agent that processes user queries and delegates
    to the appropriate tool: MongoDBTool for reads and ExternalAPI for writes.
    """
    def __init__(self):
        self.mongo = MongoDBTool()
        self.api = ExternalAPI()

    def run(self, query: str) -> str:
        """
        Process the query string and call the correct tool method.
        Returns a JSON-serializable string or message.
        """
        q = query.lower()

        # 1. Create order (e.g. "create order for Yoga for client Rohan")
        if "order for" in q and "client" in q:
            return self.api.run(query)

        # 2. List classes (e.g. "what classes are available this week?")
        if "classes" in q or "available" in q:
            return self.mongo.run(query)

        # 3. Check order status (e.g. "has order #12345 been paid?")
        if "order" in q and "#" in q and ("status" in q or "paid" in q):
            return self.mongo.run(query)

        # 4. Payment details (e.g. "show payment details for order #12345")
        if "payment" in q and "#" in q:
            return self.mongo.run(query)

        # 5. Client lookup (e.g. "get client by email abc@xyz.com")
        if any(field in q for field in ["name", "email", "phone"]):
            return self.mongo.run(query)

        return "Sorry, I couldn't understand your request."

# instantiate for FastAPI to import
support_agent = SupportAgent()
