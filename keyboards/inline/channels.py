from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

async def channels_murkup(channels):
    murkup = InlineKeyboardMarkup()
    for i,url in enumerate(channels):
        btn = InlineKeyboardButton(f"{i+1}-kanal",callback_data=f"channel_{i+1}",url=url)
        murkup.add(btn)
        
    tekshir = InlineKeyboardButton(text="✅Tekshirish",callback_data="tekshir")
    murkup.add(tekshir)
    return murkup