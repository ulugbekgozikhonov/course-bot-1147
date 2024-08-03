from aiogram import types
from loader import bot
from data.config import CHANNELS

async def user_in_channel(user_id: str):
    user_not_in_channels = []
    
    for channel_id,channel_url in CHANNELS.items():
        
        member = await bot.get_chat_member(chat_id=channel_id,user_id=user_id)
        
        if member.status in ("member","administrator","owner","creator"):
            continue
        else:
            user_not_in_channels.append(channel_url)
    
    return user_not_in_channels