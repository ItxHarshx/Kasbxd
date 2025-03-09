import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# Load bot token from environment variables
TOKEN = os.getenv("BOT_TOKEN")  # Railway will provide this

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(commands=['start'])
async def start_command(message: Message):
    await message.answer("Welcome to Arise System! Your journey begins now.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
