from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from pprint import pprint
from bot import db


class Survey(StatesGroup):
    name = State()
    age = State()
    phone_number = State()


survey_router = Router()


@survey_router.message(Command("survey"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(Survey.name)
    await message.answer("Как вас зовут?")

@survey_router.message(Survey.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await state.set_state(Survey.age)
    await message.answer("Сколько вам лет?")

@survey_router.message(Survey.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Возраст должен быть числом!")
        return
    elif int(age) < 15 or int(age) > 100:
        await message.answer("Возраст должен быть от 15 до 100!")
        return
    await state.update_data(age=int(age))
    await state.set_state(Survey.phone_number)
    await message.answer("Ваш номер телефона?")

@survey_router.message(Survey.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    await state.update_data(phone_number=phone_number)

    data = await state.get_data()
    pprint(data)
    # save to Data Base
    db.insert_survey(data)
    # чистим стейт
    await state.clear()
    await message.answer("Спасибо за пройденный опрос!")