import os

from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from dialog_flow_handler import detect_intent
from handlers import echo_message, greet_user

if __name__ == "__main__":
    load_dotenv()
    BOT_API_TOKEN = os.getenv('BOT_API_TOKEN')

    updater = Updater(BOT_API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", greet_user))
    dispatcher.add_handler(MessageHandler(Filters.text, detect_intent))

    updater.start_polling()
    updater.idle()
