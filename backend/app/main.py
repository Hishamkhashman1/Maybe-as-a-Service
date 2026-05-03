from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, create_engine, select
import os
from dotenv import load_dotenv

print("loaded dependencies")

load_dotenv()

database_url = os.getenv("database_url")

engine = create_engine(database_url)

frontend_url = "https://localhost:3000/"

app = FastAPI(
    title= "Maybe as a Service",
    version="0.1.0",
        )

app.add_middleware(
        CORSMiddleware,
        allow_origins=[frontend_url],
        allow_methods=["*"],
        allow_headers=["*"]
)


@app.get("/health")
async def health_check():
        return {"status": "ok"}

@app.get("/")
async def root():
        return {"Message": "Maybe as a Service"}


