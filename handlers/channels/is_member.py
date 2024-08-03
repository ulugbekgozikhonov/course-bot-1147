from loader import dp
from aiogram import types
from utils.misc.check_user import user_in_channel

@dp.callback_query_handler(text="tekshir")
async def check_handler(call: types.CallbackQuery):
    user_not_in_channels = await user_in_channel(call.from_user.id)
    if user_not_in_channels:
        await call.answer(text="Kanalga hali obuna bo'lmagansiz⚠️",show_alert=True)
    else:
        await call.answer(text="Kanalga obuna bo'ldingiz✅")
    