import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

TOKEN = "8668933625:AAGpmq3OKB8S1mJwS7t1Nrt0fEArqucp3MU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👔 Каталог"), KeyboardButton(text="🛒 Заказ бериш")],
        [KeyboardButton(text="📞 Оператор"), KeyboardButton(text="🚚 Доставка")]
    ],
    resize_keyboard=True
)

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "Ассалому алайкум! 👋\n\nБизда old money ва classic style кийимлар бор.",
        reply_markup=menu
    )

@dp.message(F.text == "👔 Каталог")
async def catalog(message: Message):
    await message.answer(
        "👔 Каталог:\n\n"
        "1. Classic Shirt — 250 000 сўм\n"
        "2. Old Money Polo — 300 000 сўм\n"
        "3. Classic Pants — 350 000 сўм\n\n"
        "Заказ бериш учун: 🛒 Заказ бериш"
    )

@dp.message(F.text == "🛒 Заказ бериш")
async def order(message: Message):
    await message.answer(
        "Заказ бериш учун шу форматда ёзинг:\n\n"
        "Исми: \n"
        "Телефон: \n"
        "Товар: \n"
        "Размер: \n"
        "Манзил: "
    )

@dp.message(F.text == "📞 Оператор")
async def operator(message: Message):
    await message.answer("Оператор: @username_qoy")

@dp.message(F.text == "🚚 Доставка")
async def delivery(message: Message):
    await message.answer("Доставка Тошкент бўйича бор. Нарх манзилга қараб келишилади.")

@dp.message()
async def echo(message: Message):
    await message.answer("Хабарингиз қабул қилинди ✅ Оператор тез орада боғланади.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
