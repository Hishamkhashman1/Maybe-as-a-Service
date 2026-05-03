from fastapi import FastAPI, HTTPException
from sqlmodel import Session, create_engine, select
import os
from dotenv import load_dotenv

print("loaded dependencies")

load_dotenv()

database_url = os.getenv("database_url")

engine = create_engine(database_url)

app = FastAPI()

@app.GET("/")
async def root()
#return frontend landing page

@app.get("/maybe{maybe_id}")
# return a random maybe when requested



