from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from modules.specs import Order
from modules.db import insert_order

app = FastAPI()

@app.post("/order")
async def create_order(order: Order):
    insert_order(order)
    return order

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title='Smartphone Cover Order',
        version='1.0.0',
        routes=app.routes
    )

    app.openapi_schema = openapi_schema
    return openapi_schema

app.openapi = custom_openapi
