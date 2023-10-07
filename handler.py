from commands import start, echo, duck
from filters import filter_greetings
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

def start_handler():
    return CommandHandler('start', start)

def echo_handler():
    return MessageHandler(filter_greetings & (~filters.COMMAND), echo)

def duck_handler():
    return CommandHandler('duck', duck)
# def chatgpt_handler():
#     return MessageHandler((~filters.COMMAND), chatgpt)