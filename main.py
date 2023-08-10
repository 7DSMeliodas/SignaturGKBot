from pyrogram import Client, filters
from pyrogram.types import (
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)
import asyncio
from pyrogram import enums

bot_name = 'PromoAppenderBot'
api_id = 1892826
api_hash = '2f1ad5d37f95baf2978252c0e562c551'
bot_token = '6007778653:AAH6bqeOFwKS3LuFki4glszRkLQKXDahYeQ'

bot = Client(bot_name, api_id, api_hash, bot_token)

@bot.on_message(filters.chat(-1001680674029))
async def edit_promo(c, m):
  mid = m.id
  cid = m.chat.id

  button_text = 'Unsere ☕️ Kasse freut sich!'
  button_link = 'https://t.me/Shop_System_Telegram/6/300'
  
  original_text = m.caption.markdown
  edit_with = '\n▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️\n<b>Auch Du bist ein Fan von @GruppenKanaele?</b>\n▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️'
  new_message = original_text
  new_message += edit_with
  await c.edit_message_caption(cid, mid, new_message, parse_mode=enums.ParseMode.DISABLED, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(button_text, url=button_link)]]))

bot.run()
