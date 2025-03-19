import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

# .env файлындағы мәндерді жүктеу
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Сәлем! Мен Render-де жұмыс істеп тұрған Telegram ботымын!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
