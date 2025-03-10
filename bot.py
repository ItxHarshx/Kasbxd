import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

# Load bot token from environment variables
TOKEN = os.getenv("BOT_TOKEN")

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    user_name = message.from_user.first_name  
    text = f"Hey, {user_name}! Welcome to the System! Let's get started."

    # Get bot username dynamically
    bot_info = await bot.get_me()
    bot_username = bot_info.username  

    # Inline buttons
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➕ Add Bot to Group", url=f"https://t.me/{bot_username}?startgroup=true")],
        [InlineKeyboardButton(text="🛠 Support", url="https://t.me/KaisenPortal"),
         InlineKeyboardButton(text="📣 Updates", url="https://t.me/AriseUpdates")]
    ])

    await message.answer(text, reply_markup=keyboard)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # Prevent handling old updates
    await dp.start_polling(bot)  # Start polling properly

if __name__ == "__main__":
    asyncio.run(main())
