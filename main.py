from pyrogram import Client, filters
import asyncio

bot_name = 'PromoAppenderBot'
api_id = 1892826
api_hash = '2f1ad5d37f95baf2978252c0e562c551'
bot_token = ''

bot = Client(bot_name, api_id, api_hash, bot_token)

@bot.on_message(filters.chat(-1001680674029))
async def edit_promo(c, m):
  mid = m.id
  cid = m.chat.id

  button_text = 'Unsere ☕️ Kasse freut sich!'
  button_link = 'https://t.me/Shop_System_Telegram/6/300'
  
  original_text = m.caption
  edit_with = '\n▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️\n<b>Auch Du bist ein Fan von @GruppenKanaele?</b>\n▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️'
  new_message = original_text + edit_with
  m.edit_media_caption(cid, mid, new_message, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(button_text, url=button_link)]])

bot.run()