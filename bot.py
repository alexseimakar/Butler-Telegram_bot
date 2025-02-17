from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# Чтение токена из файла
def load_token() -> str:
    with open('token.txt', 'r') as file:
        return file.read().strip()

BOT_TOKEN = load_token()


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# /start command
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer("Привет! \nМеня зовут Дух Машины! \nЯ помогаю моему разрабу найти работу и возможно, через пару апдейтов, начну ему помогать с записями идей по тематикам!")

# /help command
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer("Я пока могу только отвечать на help и start, а также передразнивать тебя :Р")

# Эхо
@dp.message()
async def reply_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)