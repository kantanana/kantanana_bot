import commands
from filters import filter_greetings
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

def start_handler():
    return CommandHandler('start', commands.start)

def echo_handler():
    return MessageHandler(filter_greetings & (~filters.COMMAND), commands.echo)

def duck_handler():
    return CommandHandler('duck', commands.duck)

def caps_handler():
    return CommandHandler('caps', commands.caps)

def unknown_handler():
    return MessageHandler(filters.COMMAND, commands.unknown)