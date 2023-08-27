import asyncio
import logging
import time

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from database.app.models import Employee, TimeTracking
from typing import List
from sqlalchemy.orm import sessionmaker, selectinload

import database.app.config_loader as config_loader
from database.app.singleton import MetaSingleton

logger = logging.getLogger(__name__)
config = config_loader.Config()


class DB(metaclass=MetaSingleton):
    def __init__(self):
        self.db_engine = self.__create_engine()

    def __create_engine(self) -> AsyncEngine:
        engine = create_async_engine(
            config.get(config_loader.DB_URI),
            echo=True,
        )
        return engine

    async def get_async_session(self) -> AsyncSession:
        async with AsyncSession(bind=self.db_engine) as session:
            yield session


async def async_main():
    config = config_loader.Config()
    engine = create_async_engine(
        config.get(config_loader.DB_URI),
        echo=True,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Employee.metadata.create_all)
        await conn.run_sync(TimeTracking.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(async_main())
