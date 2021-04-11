 # @Author: Абделлах Улахияне
# @Date:   2021-04-08 20:40:26
# @Last Modified by:   Абделлах Улахияне
# @Last Modified time: 2021-04-11 16:44:23
import telebot
from db import db
from telebot import types 
token = "1620723233:AAHcGMzHVEU_bJuUR9DMOx-j1DW_RqKDLuE"
bot = telebot.TeleBot(token)


commands = {'start':"this starts",'help':"this help's functionality","figure":"this is figures"}

# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(content_types=["text"])
def any_thing(message):
	keyboardmain = types.InlineKeyboardMarkup()
	btn1   = types.InlineKeyboardButton(text="Guide List",callback_data='guide')
	btn2   = types.InlineKeyboardButton(text="Figure List",callback_data='figue')
	keyboardmain.add(btn1,btn2)
	bot.send_message(message.chat.id,"Start",reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    
	if call.data == "back":
		keyboardmain = types.InlineKeyboardMarkup()
		btn1   = types.InlineKeyboardButton(text="Guide List",callback_data='guide')
		btn2   = types.InlineKeyboardButton(text="Figure List",callback_data='figue')
		keyboardmain.add(btn1,btn2)
		bot.edit_message_text(chat_id=call.message.chat.id,
							  message_id=call.message.message_id,
							  text="Start",reply_markup=keyboardmain)

	if call.data == 'guide':
		quidekeyboard = types.InlineKeyboardMarkup()
		btn   = types.InlineKeyboardButton(text="Back",callback_data='back')
		quidekeyboard.add(btn)
		bot.edit_message_text(chat_id=call.message.chat.id,
							  message_id=call.message.message_id,
							  text="https://www.youtube.com",reply_markup=quidekeyboard)
	if call.data == 'figure':
		figurekeyboard = types.InlineKeyboardMarkup(row_width=3)
		btns={}
		for index,figure in enumerate(db.select("figure")):
    			btns[f"btn{index+1}"]=types.InlineKeyboardButton(text=figure[1],callback_data=f"btn{index+1}")
		for i,btn in enumerate(btns):
    			figure.add(btns[btn])
		btn   = types.InlineKeyboardButton(text="Back",callback_data='back')
		quidekeyboard.add(btn)
		bot.edit_message_text(chat_id=call.message.chat.id,
							  message_id=call.message.message_id,
							  text="Figure",reply_markup=quidekeyboard)
			
    			
bot.polling()

