 # @Author: Абделлах Улахияне
# @Date:   2021-04-08 20:40:26
# @Last Modified by:   Абделлах Улахияне
# @Last Modified time: 2021-04-11 01:42:24
import telebot
from telebot import types 
token = "1620723233:AAHcGMzHVEU_bJuUR9DMOx-j1DW_RqKDLuE"
commands = {'start':"this starts",'help':"this help's functionality","figure":"this is figures"}

bot = telebot.TeleBot(token)
# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=commands)
def text(message):
	bot.send_message(message.chat.id, commands[message.text[1:]])


bot.polling()

