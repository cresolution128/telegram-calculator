"""Minimal aiogram 3 bot that opens the WebApp calculator.

    pip install aiogram
    set BOT_TOKEN=...   &&  set WEBAPP_URL=https://<user>.github.io/<repo>/
    python bot.py
"""
import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    KeyboardButton, Message, ReplyKeyboardMarkup, WebAppInfo,
)

BOT_TOKEN = os.environ["BOT_TOKEN"]
WEBAPP_URL = os.environ["WEBAPP_URL"]  # must be https

dp = Dispatcher()

kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(
        text="📊 Open calculator",
        web_app=WebAppInfo(url=WEBAPP_URL),
    )]],
    resize_keyboard=True,
)


@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        "Tender lot profitability calculator.\n"
        "Tap the button below, run the numbers, and send the result back to this chat.",
        reply_markup=kb,
    )


@dp.message(F.web_app_data)
async def on_webapp_data(message: Message) -> None:
    # text produced by tg.sendData() in the WebApp — a ready-made summary
    await message.answer(f"<pre>{message.web_app_data.data}</pre>", parse_mode="HTML")


async def main() -> None:
    await dp.start_polling(Bot(BOT_TOKEN))


if __name__ == "__main__":
    asyncio.run(main())
