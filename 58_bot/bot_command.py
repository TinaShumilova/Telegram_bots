from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/delete\n/help\n')

def deleted_command(update: Update, context: CallbackContext):
    str = update.message.text
    print(str)
    tr = str.split()
    print(tr)
    tr.remove(tr[0])
    print(tr)
    [tr.remove(word) for word in tr[:] if 'абв' in word]
    print(tr)
    text = ''.join(tr)
    update.message.reply_text(f'результат = {text}')
