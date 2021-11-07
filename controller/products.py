# import library
import datetime
from fastapi import APIRouter
from pymongo import database, results
from models.schemas import *
from mongoengine import connect
from models.schemas import *
from config.database import *

product_route = APIRouter()

@product_route.post("/setproduct", tags=["Testing NFC"])
async def set_items(product: Products):
    db = Database()
    product.items.creation_date = datetime.now()
    result = db.Create_product(product)
    return result

@product_route.get("/getproducts", tags=["Testing NFC"])
async def Get_items():
    db = Database()
    result = db.Get_products()
    return result