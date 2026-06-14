import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, FSInputFile

import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
ADMIN_ID = 8874206770
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍  Каталог"), KeyboardButton(text="🛒 Заказ бериш")],
        [KeyboardButton(text="📞 Оператор"), KeyboardButton(text="🚚 Доставка")]
    ],
    resize_keyboard=True
)


@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "Ассалому алайкум ва раҳматуллоҳи ва баракатух! 👋\n\n"
        "Sadi Style бутига хуш келибсиз.\n\n"
        "Бу ерда сиз тез ва ишончли тарзда кийимларга заказ беришингиз мумкин.\n\n"
        "✅ Наличида бор маҳсулотлар: 1–3 кун ичида етказиб берилади.\n"
        "📦 Под заказ маҳсулотлар: 7–10 кун ичида етказиб берилади.\n\n"
        "Керакли бўлимни танланг 👇",
        reply_markup=menu
    )


@dp.message(F.text == "🛍 Каталог")
async def catalog(message: Message):
    media = [
        FSInputFile("shoes.jpg"),
        FSInputFile("hoodie.jpg"),
        FSInputFile("shorts.jpg")
    ]

    captions = [
        "🤍 Oq Krossovkan 👟 450 000 so'm",
        "🤍 Oq Ko'ylak (Hoodie) 280 000 so'm",
        "🤍 Oq Ko'ylak va Shorti 350 000 so'm"
    ]

    for i in range(len(media)):
        await message.answer_photo(
            photo=media[i],
            caption=captions[i]
        )

@dp.message(F.text == "🛒 Заказ бериш")
async def order(message: Message):
    await message.answer(
        "🛒 Заказ бериш учун шу форматда ёзинг:\n\n"
        "Исми:\n"
        "Телефон:\n"
        "Товар:\n"
        "Размер:\n"
        "Манзил:"
    )


@dp.message(F.text == "📞 Оператор")
async def operator(message: Message):
    await message.answer("📞 Оператор: +998504449994")


@dp.message(F.text == "🚚 Доставка")
async def delivery(message: Message):
    await message.answer(
        "🚚 Доставка:\n\n"
        "Тошкент бўйича доставка бор.\n"
        "Нарх манзилга қараб келишилади."
    )


@dp.message(F.text)
async def all_messages(message: Message):
    if message.text in ["🛍  Каталог", "🛒 Заказ бериш", "📞 Оператор", "🚚 Доставка", "/start"]:
        return

    user = message.from_user
    username = f"@{user.username}" if user.username else "Username yo'q"

    await bot.send_message(
        ADMIN_ID,
        f"🆕 Янги заказ!\n\n"
        f"👤 Клиент: {user.full_name}\n"
        f"🔗 Username: {username}\n"
        f"🆔 Telegram ID: {user.id}\n\n"
        f"✉️ Заказ матни:\n{message.text}"
    )

    await message.answer(
        "✅ Заказингиз қабул қилинди.\n"
        "Оператор тез орада сиз билан боғланади.",
        reply_markup=menu
    )


async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
