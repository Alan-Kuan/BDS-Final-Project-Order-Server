from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import sys
import uvicorn

from modules.specs import Order
from modules.db import insert_order, get_all_orders

if __name__ == '__main__':
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print(f'Usage: {sys.argv[0]} <dev|prod> [domain name]')
        exit(1)

    if sys.argv[1] == 'dev':
        port = 8000
        host = '127.0.0.1'
    elif sys.argv[1] == 'prod':
        port = 80
        host = '0.0.0.0'
    else:
        print(f'Usage: {sys.argv[0]} <dev|prod> [domain name]')
        exit(1)

    app = FastAPI()

    @app.post('/order')
    async def create_order(order: Order):
        insert_order(order)
        return order

    @app.get('/order')
    async def get_order():
        return get_all_orders()

    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = get_openapi(
            title='Smartphone Cover Order',
            version='1.0.0',
            routes=app.routes
        )
        if sys.argv[1] == 'prod' and sys.argv[2]:
            openapi_schema['servers'] = [
                {
                    'url': sys.argv[2],
                    'description': 'production server'
                },
            ]

        app.openapi_schema = openapi_schema
        return openapi_schema

    app.openapi = custom_openapi
    uvicorn.run(app, port=port, host=host)
