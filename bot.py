import logging
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Указываем токен вашего бота
API_TOKEN = 'Token'

# Создаем экземпляры бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

router = Router()

# Обработчик команды /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Я в рот это всё ебал, блять")

# Регистрация роутера
dp.include_router(router)

# Запуск бота
if __name__ == '__main__':
    from aiogram.utils import executor
    executor.start_polling(dp, skip_updates=True)