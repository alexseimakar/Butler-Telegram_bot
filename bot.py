from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
import requests

# Чтение токена из файла
def load_token() -> str:
    with open('token.txt', 'r') as file:
        return file.read().strip()

CATS_API_URL = "https://api.thecatapi.com/v1/images/search" #API рандомное фото котика
BOT_TOKEN = load_token()


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# /start command
async def process_start_command(message: Message):
    await message.answer("Привет! \nМеня зовут Дух Машины! \nЯ помогаю моему разрабу найти работу и возможно, через пару апдейтов, начну ему помогать с записями идей по тематикам!")

# /help command
async def process_help_command(message: Message):
    await message.answer("Я пока могу только отвечать на help и start, а также передразнивать тебя :Р")

# Эхо фото
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)
# Эхо
async def reply_echo(message: Message):
    await message.reply(text=message.text)

# Рандомный котик
async def send_cat_APIcall(message: Message):
    response = requests.get(CATS_API_URL)
    await message.answer(response.json()[0]["url"])


dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_cat_APIcall, Command(commands='cat'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(reply_echo)

if __name__ == '__main__':
    dp.run_polling(bot)