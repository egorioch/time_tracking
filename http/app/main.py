import uvicorn
import logging

from fastapi import FastAPI, Depends
import config_loader as config_loader
from database.app.db import DB
from database.app.models import Employee, TimeTracking

config = config_loader.Config()
app = FastAPI()

logging.basicConfig(
    level=logging.getLevelName(config.get(config_loader.LOGGING_LEVEL)),
    format=config.get(config_loader.LOGGING_FORMAT)
)

logger = logging.getLogger("uvicorn.error")

""" Возвращает весь массив объектов таблицы time_tracking
"""


@app.get("/all_time")
async def get_all_time(db_instance: DB = Depends()):
    async with db_instance.get_async_session() as session:
        pass


if __name__ == "__main__":
    logger.info("STARTING SERVER")
    uvicorn.run(
        app,
        port=config.get(config_loader.WEB_PORT),
        host=config.get(config_loader.WEB_HOST)
    )
