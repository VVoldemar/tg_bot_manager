import os
import asyncio
import aiogram
import dotenv
import logging

import routers
import settings

from models import db_session

dotenv.load_dotenv()

bot = aiogram.Bot(token=os.getenv("TOKEN"))
dp = aiogram.Dispatcher()

async def main():
    db_session.global_init(settings.DB_FILE)
    dp.include_routers(*routers.routers)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')