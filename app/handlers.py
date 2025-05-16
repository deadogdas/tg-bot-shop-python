from aiogram import F,Router
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart,Command
import app.keyboards as kb
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
import app.database.requests as rq
from app.keyboards import categories

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer("Добро пожаловать!",reply_markup=kb.main)

@router.message(F.text=='Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара',reply_markup=await kb.categories())

@router.callback_query(F.data.startswith('category_'))
async def category(callback:CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите товар по категории',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))

@router.callback_query(F.data.startswith('item_'))
async def item(callback:CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    if not item_data:
        await callback.answer("Товар не найден")
        return
    await callback.message.answer(
        f'Название: {item_data.name}\n'
        f'Описание: {item_data.description}\n'
        f'Цена: {item_data.price}$'
    )