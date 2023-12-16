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
