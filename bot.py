import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, FSInputFile

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Меню
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Каталог"), KeyboardButton(text="🛒 Заказ бериш")],
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


# 🛍 Каталог
@dp.message(F.text == "🛍 Каталог")
async def catalog(message: Message):
    items = [
        ("shoes.jpg",  "🤍 Oq Krossovkan 👟 450 000 so'm"),
        ("hoodie.jpg", "🤍 Oq Ko'ylak (Hoodie) 280 000 so'm"),
        ("shorts.jpg", "🤍 Oq Ko'ylak va Shorti 350 000 so'm"),
    ]

    for photo_name, caption in items:
        await message.answer_photo(
            photo=FSInputFile(photo_name),
            caption=caption
        )


# 🛒 Заказ бериш
@dp.message(F.text == "🛒 Заказ бериш")
async def order(message: Message):
    await message.answer(
        "Заказ бериш учун каталогдаги товар рақамини ёзиб қолдиринг "
        "ёки '📞 Оператор' тугмасини босинг."
    )


# 📞 Оператор
@dp.message(F.text == "📞 Оператор")
async def operator(message: Message):
    await message.answer("Оператор билан боғланиш учун: +998 ** *** ** **")


# 🚚 Доставка
@dp.message(F.text == "🚚 Доставка")
async def delivery(message: Message):
    await message.answer("Доставка: Тошкент бўйлаб 1–3 кун, бошқа шаҳарларга 3–7 кун.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

