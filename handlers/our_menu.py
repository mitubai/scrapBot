from bot import db
from aiogram import Router, F, types
from pathlib import Path


menu_router = Router()

@menu_router.callback_query(F.data == "our_menu")
async def make_order(callback: types.CallbackQuery):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [

            ]
        ]
    )
    await callback.message.answer("Что пожелаете?", reply_markup=kb)


dishes_categories = ("закуски", "салаты", "супы", "пицца 30 см", "пицца 40 см")
@menu_router.message(F.text.lower().in_(dishes_categories))
async def show_dishes_of_category(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    category = db.get_category_by_name(message.text)
    dishes = db.get_dishes_by_cat_name(message.text)
    await message.answer(category[2])
    for dish in dishes:
        file_path = Path(__file__).parent.parent / "images" / dish[4]
        file = types.FSInputFile(file_path)
        caption = f"Название{dish[1]}\nОписание: {dish[2]}\nЦена: {dish[3]}"
        await message.answer_photo(file, caption=caption)
