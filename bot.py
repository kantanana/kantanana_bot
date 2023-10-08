from telegram.ext import ApplicationBuilder
import os
telebot_key = os.environ['TELEBOT']

application = ApplicationBuilder().token(telebot_key).build()
