from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os
from sample.env import BOT_TOKEN
# Load bot token from environment variables (for security)
TOKEN = os.getenv("BOT_TOKEN")  # Set this in Railway later

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    await message.answer("Welcome to Arise System! Your journey begins now.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
