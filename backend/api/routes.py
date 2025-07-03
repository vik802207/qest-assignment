from fastapi import APIRouter, Request
from agents.support_agent import support_agent
from tools.mongodb_tool import is_mongo_connected
from tools.payment_api import add_payment
from tools.add_entity import add_client, add_order, add_payment, add_course, add_class
router = APIRouter()

@router.post("/query/support")
async def query_support(request: Request):
    body = await request.json()
    result = support_agent.run(body.get("query", ""))
    return {"response": result}


@router.get("/health/mongo")
def check_mongo():
    ok = is_mongo_connected()
    return {"mongo_connected": ok}
@router.post("/payments/add")
async def create_payment(request: Request):
    data = await request.json()
    order_id = data.get("order_id")
    amount = data.get("amount")
    date = data.get("date")  # optional

    result = add_payment(order_id, amount, date)
    return {"result": result}

@router.post("/add/client")
async def create_client(request: Request):
    return {"result": add_client(await request.json())}

@router.post("/add/order")
async def create_order(request: Request):
    return {"result": add_order(await request.json())}

@router.post("/add/payment")
async def create_payment(request: Request):
    return {"result": add_payment(await request.json())}

@router.post("/add/course")
async def create_course(request: Request):
    return {"result": add_course(await request.json())}

@router.post("/add/class")
async def create_class(request: Request):
    return {"result": add_class(await request.json())}
