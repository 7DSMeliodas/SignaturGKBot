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
  
  original_text = m.caption.html
  edit_with = '\n\n▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️\n<b>Auch Du bist ein Fan von @GruppenKanaele?</b>\n▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️'
  new_message = original_text
  new_message += edit_with
  await c.edit_message_caption(cid, mid, new_message, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(button_text, url=button_link)]]))

@bot.on_message(filters.chat(-1001389504085))
async def edit_promo_2(c, m):
  mid = m.id
  cid = m.chat.id
    
  original_text = m.caption.html
  edit_with = '\n\n<b>Eine Zensur findet <s>nicht</s> statt</b> <b>😱</b>\n<a href='https://t.me/Metapedia_Deutsch/1173'>Art. 5 Grundgesetz</a>\n\n➡️ <a href='https://t.me/EchteNachrichten'>Echte Nachrichten</a>\n➡️ <a href='https://t.me/News_World_International'>Real News International</a>\n➡️ <a href='https://t.me/AlternativeMedien'>Freie Medien</a>\n➡️ <a href='https://t.me/Prozessbeobachter'>\(Un\)Rechtswesen</a>\n➡️ <a href='https://t.me/Corona_Reset'>Unzensierte Querschau</a>\n➡️ <a href='https://t.me/gesperrtBRD'>Gelöschtes hochladen</a>\n\n<b>Sehen, was gesperrt ist</b>\n<b>@Medienzensur</b>'
  new_message = original_text
  new_message += edit_with

  await c.edit_message_caption(cid, mid, new_message, parse_mode=enums.ParseMode.HTML)
bot.run()
