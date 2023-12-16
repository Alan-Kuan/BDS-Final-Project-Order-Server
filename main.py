from fastapi import FastAPI
from modules.specs import Order
from modules.db import insert_order

app = FastAPI()

@app.post("/order")
async def create_order(order: Order):
    insert_order(order)
    return order
