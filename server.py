from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from bot_manager import BotManager

app = FastAPI(title="Agar Engine", version="0.2.0")
manager = BotManager()


class CreateBotsRequest(BaseModel):
    count: int = Field(default=50, ge=1, le=50)
    nickname_prefix: str = Field(default="Bot", min_length=1, max_length=20)


class TargetRequest(BaseModel):
    uid: str = Field(min_length=1, max_length=128)


@app.get("/")
def home():
    return {
        "name": "Agar Engine",
        "status": "running",
        "managed_bots": len(manager.bots),
    }


@app.post("/bots")
def create_bots(request: CreateBotsRequest):
    manager.create_bots(request.count, request.nickname_prefix)
    return {
        "message": "Bot records created",
        "count": len(manager.bots),
    }


@app.get("/bots")
def list_bots():
    return manager.status()


@app.post("/target")
def set_target(request: TargetRequest):
    if not manager.bots:
        raise HTTPException(status_code=400, detail="Create bot records first.")

    manager.set_target(request.uid)
    return {
        "message": "Target assigned",
        "target_uid": request.uid,
    }


@app.post("/start")
def start_bots():
    if not manager.bots:
        raise HTTPException(status_code=400, detail="Create bot records first.")

    manager.start_all()
    return {
        "message": "Game connections are not implemented yet.",
        "count": len(manager.bots),
        "state": "not_implemented",
    }


@app.post("/stop")
def stop_bots():
    manager.stop_all()
    return {
        "message": "All bot records stopped.",
        "count": len(manager.bots),
        "state": "stopped",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
