# -*- coding: utf-8 -*-
import os
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
#r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging 

updater = Updater(token=token)
dispatcher = updater.dispatcher

logging.basicConfig(
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	level=logging.INFO)


def start(bot,update):
	bot.send_message(chat_id=update.message.chat_id, text="This is where we would trigger adding users")

start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)
