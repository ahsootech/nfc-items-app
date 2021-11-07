from jose.jws import verify
from pydantic.utils import Obj
from pymongo import MongoClient, results, DESCENDING
from random import randint
from models.schemas import *
from bson import ObjectId, json_util
from pymongo.errors import DuplicateKeyError
from fastapi import Depends, FastAPI, HTTPException, status
from mongoengine import NotUniqueError
from typing import List
from bson.json_util import dumps
from bson.json_util import loads
from config.config import dbconfig
import json

class Database:
    mydb = None

    def __init__(self):
        # Step 1: Connect to MongoDB - Note: Change connection string as needed
        # mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
        config = dbconfig()
        self.mydb = config.mydb

    # def login_user(self, username, password):
    #     mycursor = self.mydb.cursor()
    #     mycursor.execute("SELECT * FROM users WHERE username = '" +
    #                      username + "' AND password = '" + password + "'")
    #     myresult = mycursor.fetchone()
    #     if(myresult is not None):
    #         print(myresult)
    #         user = NewUser(username=myresult[0], password=myresult[1],
    #                        firstname=myresult[2], lastname=myresult[3])
    #         return user
    #     else:
    #         return None

    #     return myresult

    def Create_product(self, product: Products):
        try:
            product = json.loads(product.json())
            result = self.mydb.products.insert_one(product)
            print(result.inserted_id)
            product = {"name": product['items']["name"], "detail": str(
                "Registration Successfully check the email ID")}
            return product
        except (NotUniqueError, DuplicateKeyError):
            return {"name": product.items.name, "detail": str("Already Taken this Email ID")}

    def Get_products(self):
        try:
            result = self.mydb.products.find()
            products = []
            for product in result:
                json_doc = json.dumps(product, default=json_util.default)
                products.append(json.loads(json_doc))
            return {"details": "Successfully", "products": products}
        except Exception as e:
            return {"details": str(e), "statuscode": 400}
