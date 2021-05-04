from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from src.bot.keyboards import keyboard_after_quiz
from src.bot.misc import bot
from src.bot.utils import texts, text_formater
from src.core.settings import Settings
from src.core.tables import get_by_id_quiz, AfterQuiz, update_current_quiz_sent


async def quiz_callback(callback: CallbackQuery, state: FSMContext):
    t = callback.data.split('_')
    status_index = int(t[0])
    quiz_id = int(t[1])

    quiz: AfterQuiz = get_by_id_quiz(quiz_id)
    if quiz is None:
        print('quiz does not exist')

    status = texts.statuses[status_index]

    quiz.status = status
    update_current_quiz_sent(quiz)

    temp_statuses = texts.statuses_to_btn
    if status_index == len(texts.statuses)-1:
        keyboard = None
    else:

        keyboard = await keyboard_after_quiz(temp_statuses, quiz_id, index_to_pass=status_index)
    if quiz.type_number == 1:
        text = text_formater.get_text_after_quiz(quiz)
    else:
        text = text_formater.get_text_back_call(quiz)
    await bot.edit_message_text(text, callback.message.chat.id, callback.message.message_id, reply_markup=keyboard)


