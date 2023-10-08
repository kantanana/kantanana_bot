from commands import start, echo, duck, caps
from filters import filter_greetings
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

def start_handler():
    return CommandHandler('start', start)

def echo_handler():
    return MessageHandler(filter_greetings & (~filters.COMMAND), echo)

def duck_handler():
    return CommandHandler('duck', duck)

def caps_handler():
    return CommandHandler('caps', caps)