from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


async def on_startup(_):
    print('Я запустился!')

if __name__ == "__main__":
    from handlers import dp
    while True:
        try:
            executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
        except Exception as e:
            print(e)
