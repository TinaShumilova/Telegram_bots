from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from bot_command import *


updater = Updater('')

updater.dispatcher.add_handler(CommandHandler('delete', deleted_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
#.dispatcher.add_handler(CommandHandler('game', game_command))
#updater.dispatcher.add_handler(CommandHandler('temp', temp))
#updater.dispatcher.add_handler(MessageHandler(Filters.text, temp))


print('server start')
updater.start_polling()
updater.idle()
