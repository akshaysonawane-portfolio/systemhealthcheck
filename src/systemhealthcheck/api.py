from fastapi import FastAPI
from systemhealthcheck import get_health

app = FastAPI(title="System Health Monitor")

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/health")
def health():
    return get_health()
