from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from pymongo import MongoClient
from datetime import datetime
import pytz
import os, json
from dotenv import load_dotenv

app = FastAPI(title="Multi-Agent Backend")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]

# Timezone
india_tz = pytz.timezone("Asia/Kolkata")
@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.post("/query/dashboard")
async def query_dashboard(request: Request):
    body = await request.json()
    query = body.get("query", "").lower()
    now = datetime.now(india_tz)

    # Revenue this month
    if "revenue" in query and "this month" in query:
        month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        payments = db.payments.aggregate([
            {"$match": {"date": {"$gte": month_start}}},
            {"$group": {
                "_id": None,
                "total": {"$sum": "$amount"},
                "count": {"$sum": 1}
            }}
        ])
        data = list(payments)
        if data:
            return {
                "response": f"This month revenue: ₹{data[0]['total']} from {data[0]['count']} payments."
            }
        return {"response": "No payments found for this month."}

    # Inactive clients
    elif "inactive clients" in query:
        total = db.clients.count_documents({})
        inactive = db.clients.count_documents({"status": "inactive"})
        return {"response": f"Inactive clients: {inactive} out of {total}."}

    # Top enrolled course
    elif "highest enrollment" in query or "top services" in query:
        result = list(db.courses.aggregate([
            {"$project": {
                "name": 1,
                "enrollments": {"$size": "$enrolled_clients"}
            }},
            {"$sort": {"enrollments": -1}},
            {"$limit": 1}
        ]))
        if result:
            return {
                "response": f"Top enrolled course: {result[0]['name']} with {result[0]['enrollments']} enrollments."
            }
        return {"response": "No course data found."}

    # Attendance percentage
    elif "attendance percentage" in query:
        if "for" in query:
            class_name = query.split("for")[-1].strip()
            total = db.attendance.count_documents({"class_name": class_name})
            present = db.attendance.count_documents({"class_name": class_name, "status": "present"})
            if total == 0:
                return {"response": f"No attendance records found for {class_name}."}
            percent = (present / total) * 100
            return {
                "response": f"Attendance percentage for {class_name}: {percent:.2f}%"
            }
        return {"response": "Please specify class name after 'for'."}

    return {"response": "Query not recognized. Try revenue, inactive clients, top course, or attendance."}
