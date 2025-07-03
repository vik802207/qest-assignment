from pydantic import BaseModel

class Client(BaseModel):
    name: str
    email: str
    phone: str
    status: str = "active"
    enrolled_courses: list[str] = []
