from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your bot.")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This is a help message.")

def main():
    updater = Updater(token='YOUR_BOT_TOKEN_HERE', use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    updater.start_polling()

if __name__ == '__main__':
    main()
