from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline.channels import channels_murkup
from filters.is_private import IsPrivateChat
from utils.misc.check_user import user_in_channel

@dp.message_handler(CommandStart(),IsPrivateChat())
async def bot_start(message: types.Message):
    channels = await user_in_channel(message.from_user.id)
    if channels:
        await message.answer("Botimizdan foydalanish uchun rasmiy kanalimizga <b>obuna bo'ling</b> va <b>Tekshirish</b> tugmasini bosing.",
                             reply_markup=await channels_murkup(channels))
    else:
        await message.answer("Xush kelibsiz")