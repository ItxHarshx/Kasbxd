import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# Load bot token from environment variables
TOKEN = os.getenv("BOT_TOKEN")

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))  # Correct command handler
async def start_command(message: Message):
    await message.answer("Welcome to Arise System! Your journey begins now.")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # Prevent handling old updates
    await dp.start_polling(bot)  # Start polling without incorrect include_router()

if __name__ == "__main__":
    asyncio.run(main())
