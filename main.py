from bot import application
from log import logger
from handler import start_handler, echo_handler, duck_handler, caps_handler


if __name__ == '__main__':
    application.add_handler(start_handler())
    application.add_handler(echo_handler())
    application.add_handler(duck_handler())
    application.add_handler(caps_handler())
    
    application.run_polling()