import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

# Load bot token from environment variables
TOKEN = os.getenv("BOT_TOKEN")

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Function to generate the main menu
async def send_main_menu(message_or_callback):
    text = f"Hey {message_or_callback.from_user.first_name}, Welcome to Arise System! Click on the buttons below for more options."

    bot_info = await bot.get_me()
    bot_username = bot_info.username  

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➕ Add Bot to Group", url=f"https://t.me/{bot_username}?startgroup=true")],
        [InlineKeyboardButton(text="📢 Updates", url="https://t.me/YOUR_UPDATES_CHANNEL"),
         InlineKeyboardButton(text="🛠 Support", url="https://t.me/YOUR_SUPPORT_GROUP")],
        [InlineKeyboardButton(text="❓ How to Use? Command Menu", callback_data="how_to_use")]
    ])

    if isinstance(message_or_callback, Message):
        await message_or_callback.answer(text, reply_markup=keyboard)
    else:  # If it's a callback query
        await message_or_callback.message.edit_text(text, reply_markup=keyboard)

# Start command handler
@dp.message(Command("start"))
async def start_command(message: Message):
    await send_main_menu(message)

# Callback handler for "How to Use?"
@dp.callback_query(lambda c: c.data == "how_to_use")
async def how_to_use_callback(callback_query: CallbackQuery):
    text = """📌 *Command Menu*:

Click "Back" to return."""

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Back", callback_data="back_to_start")]
    ])

    await callback_query.message.edit_text(text, reply_markup=keyboard)

# Callback handler to go back to the start
@dp.callback_query(lambda c: c.data == "back_to_start")
async def back_to_start(callback_query: CallbackQuery):
    await send_main_menu(callback_query)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # Prevent handling old updates
    await dp.start_polling(bot)  # Start polling properly

if __name__ == "__main__":
    asyncio.run(main())
