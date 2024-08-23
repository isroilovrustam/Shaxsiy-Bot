from aiogram.dispatcher.filters.state import StatesGroup, State


class ReklamaState(StatesGroup):
    message = State()  # ism


class CourseState(StatesGroup):
    full_name = State()
    phone_number = State()
    username = State()
    course_title = State()
    course_type = State()

