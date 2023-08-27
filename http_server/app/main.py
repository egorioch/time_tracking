from typing import Sequence

import uvicorn
import logging

from fastapi import FastAPI, Depends
from http_server.app import config_loader as config_loader
from database.app.db import DB
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from http_server.app.models import TimeTracking, Employee

config = config_loader.Config()
app = FastAPI()
db_instance = DB()

logging.basicConfig(
    level=logging.getLevelName(config.get(config_loader.LOGGING_LEVEL)),
    format=config.get(config_loader.LOGGING_FORMAT)
)

logger = logging.getLogger("uvicorn.error")


@app.get("/time_tracking/all", response_model=list[TimeTracking])
async def get_all_time(session: AsyncSession = Depends(db_instance.get_async_session)) -> list[TimeTracking]:
    result = await session.execute(select(TimeTracking))
    return result.scalars().all()

if __name__ == "__main__":
    logger.info("STARTING SERVER")
    uvicorn.run(
        app,
        port=config.get(config_loader.WEB_PORT),
        host=config.get(config_loader.WEB_HOST)
    )
