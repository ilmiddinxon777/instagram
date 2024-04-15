from aiogram.dispatcher.filters.state import State,StatesGroup

class Forma(StatesGroup):
    ism_qabul_qilish = State()
    familiya_qabul_qilish = State()
    yosh_qabul_qilish = State()
    tel_qabul_qilish = State()
    murojaat_qabul = State()
    tastq_qabul_qilish = State()