from telegram.ext import ApplicationBuilder, CommandHandler
from log import logger
from handler import start_handler, echo_handler, duck_handler
import os
telebot_key = os.environ['TELEBOT']

if __name__ == '__main__':
    application = ApplicationBuilder().token(telebot_key).build()

    application.add_handler(start_handler())
    application.add_handler(echo_handler())
    application.add_handler(duck_handler())
    # application.add_handler(chatgpt_handler())
    
    application.run_polling()