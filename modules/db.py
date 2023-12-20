from tinydb import TinyDB
from modules.specs import Order

db = TinyDB('db.json')

def insert_order(order: Order):
    db.insert(order.model_dump())

def get_all_orders():
    return db.all()
