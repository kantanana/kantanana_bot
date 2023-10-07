from telegram.ext import ApplicationBuilder, CommandHandler
from log import logger
from handler import start_handler, echo_handler


if __name__ == '__main__':
    application = ApplicationBuilder().token('6674542557:AAHWwRG6kuCChqkhzExRqpeVfgLczM20hUg').build()

    application.add_handler(start_handler())
    application.add_handler(echo_handler())
    # application.add_handler(chatgpt_handler())
    
    application.run_polling()