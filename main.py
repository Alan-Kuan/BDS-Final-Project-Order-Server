from fastapi import FastAPI
from pydantic import BaseModel

class Customer(BaseModel):
    name: str
    addr: str
    phone: str
    email: str | None = None

class Order(BaseModel):
    desc: str
    img_uri: str
    customer: Customer

app = FastAPI()

@app.post("/order")
async def create_order(order: Order):
    # TODO: add to a db
    return order
