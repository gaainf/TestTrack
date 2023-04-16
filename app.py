from db import db
from fastapi import FastAPI


app = FastAPI(title="TestTrack API", description="TestTrack Open API")


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
