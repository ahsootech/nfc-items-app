from datetime import datetime, timedelta
from typing import List, Optional
from bson import objectid
from bson.objectid import ObjectId
from mongoengine import *
from pydantic import BaseModel


class Items(BaseModel):
    name: str
    creation_date: Optional[datetime] = None
    price: int
    description: str
    quantity: int

class Products(BaseModel):
    items: Items
    decryption_key: str


