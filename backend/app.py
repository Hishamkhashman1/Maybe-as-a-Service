import fastapi as FastAPI

app = FastAPI()

@app.get
def get_health():
    return {"message":"maybe everything is ok?"}
