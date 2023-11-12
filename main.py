from bot import application
from log import logger
import handler


if __name__ == '__main__':
    application.add_handler(handler.start_handler())
    application.add_handler(handler.echo_handler())
    application.add_handler(handler.duck_handler())
    application.add_handler(handler.caps_handler())
    application.add_handler(handler.unknown_handler())
    
    application.run_polling()