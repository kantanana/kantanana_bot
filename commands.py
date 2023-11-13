from telegram import Update
from telegram.ext import ContextTypes
import requests
from filters import filter_greetings

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm kantana, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text=filter_greetings.detect(message.text)+' '+
filter_greetings.name_presence(message.text,
                            message.from_user), 
                            parse_mode="Markdown")

async def duck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    req = requests.get('https://random-d.uk/api/v2/randomimg').content
    with open('duck.png', 'wb') as f:
        f.write(req)
    await context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=open('duck.png', 'rb'))
    # await context.bot.send_message(chat_id=update.effective_chat.id, text='https://random-d.uk/api/v2/randomimg')

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

async def capture(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = ' '.join(context.args).lower()
    await context.bot.send_message(chat_id=update.effective_chat.id, text='')
    

