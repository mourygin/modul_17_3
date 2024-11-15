from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, List
import sys
from routers import task
from routers import user

app = FastAPI()
app.include_router(task.router)
app.include_router(user.router)

@app.get("/")
async def welcome(request: Request) -> HTMLResponse:
    return {"message": "Welcome to Taskmanager"}
