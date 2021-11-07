from datetime import datetime, timedelta
from typing import Optional, List
import json
from collections import namedtuple
from json import JSONEncoder
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from controller.products import *

tags_metadata = [
    {
        "name": "Testing NFC",
        "description": "Development Sever for NFC Android Application.",
    }
]
app = FastAPI(openapi_tags=tags_metadata,
              title="Fast API - Testing NFC",
              description="This is a testing API Development Server, Author: Muhammad Ahsan Shamim",
              version="1.0.0",)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(product_route)


@app.get("/", tags=["Testing NFC"])
async def API_HUB():
    return {"Testing NFC": "Development Server"}

