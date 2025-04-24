import os
import asyncio
import aiogram
import dotenv
import logging

import routers

dotenv.load_dotenv()

bot = aiogram.Bot(token=os.getenv("TOKEN"))
dp = aiogram.Dispatcher()

async def main():
    dp.include_routers(*routers.routers)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')