from telegram import Update
from telegram.ext import ContextTypes
import requests
# from gpt import question

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def duck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    req = requests.get('https://random-d.uk/api/v2/randomimg')
    img = req.raw.read()
    with open('duck.png', 'w') as f:
        f.write(img)
    await context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=open('duck.png', 'rb'))
    

# async def chatgpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=question(update.message.text))
