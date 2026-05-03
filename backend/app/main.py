from fastapi import FastAPI, HTTPException
from sqlmodel import Session, create_engine, select
import os
from dotenv import load_dotenv

print("loaded dependencies")



