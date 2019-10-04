import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import json


def start(update, context):
    context.bot.send_message(update.message.chat_id, text='WAH')


def answer(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='WAH')


def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                     text='Sorry, I didn\'t understand that WAH! Speak clearly, bitch!')


def main():
    with open('config.json', 'r') as fp:
        config = json.load(fp)
    ciccia = telegram.Bot(token=config['token'])
    print(ciccia.get_me())

    updater = Updater(token=config['token'], use_context=True)

    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    answ_handler = MessageHandler(Filters.regex('gay'), answer)
    dispatcher.add_handler(answ_handler)

    unk_handler = MessageHandler(Filters.text, unknown)
    dispatcher.add_handler(unk_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
