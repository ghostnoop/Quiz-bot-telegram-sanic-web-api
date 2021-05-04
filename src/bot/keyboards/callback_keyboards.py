from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def keyboard_after_quiz(statuses, quiz_id, index_to_pass=None) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    for index, status in enumerate(statuses):
        if index_to_pass >= index:
            continue

        keyboard.add(InlineKeyboardButton(status, callback_data=f'{index}_{quiz_id}'))
    return keyboard
