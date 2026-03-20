import asyncio
import logging

from fastapi import FastAPI


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)

app = FastAPI()

db_ready = False


async def connect_to_db():
    global db_ready
    await asyncio.sleep(20)  # типа долгое подключение
    db_ready = True
    logger.info("Успешно подключились к базе")


@app.on_event("startup")
async def on_startup():
    asyncio.create_task(connect_to_db())


@app.get("/")
def hello():
    logger.info("Подпишись на канал Артёма Шумейко")
    return {"ok": True}


@app.get("/health")
def health():
    logger.info("Вызов /health эндпоинта")
    if db_ready:
        logger.info("База готова!")
        return {"status": "ok"}
    logger.info("База не готова")
    return {"status": "starting"}, 500