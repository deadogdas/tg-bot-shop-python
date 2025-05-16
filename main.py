import asyncio
from aiogram import Bot,Dispatcher
from app.handlers import router
from app.database.models import async_main

async def main():
    await async_main()
    bot = Bot(token="7961088770:AAFXoryK8tk2rI7skR0e2udL_SPJqIO6uSE")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
