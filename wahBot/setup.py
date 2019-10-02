import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


def start(bot, update):
    bot.send_message(update.message.chat_id, text='WAH')


def answer(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='WAH')


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that WAH! Speak clearly, bitch!")


def main():
    ciccia = telegram.Bot(token='123456789:ASDFGHJKLÒZXCVBNMQWcdByHoYDTsMnxDY') # Sample Token
    print(ciccia.get_me())

    updater = Updater(token='123456789:ASDFGHJKLÒZXCVBNMQWcdByHoYDTsMnxDY') # Sample Token

    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    answ_handler = MessageHandler(Filters.regex('gay'), answer)
    dispatcher.add_handler(answ_handler)

    unk_handler = MessageHandler(Filters.text, unknown)
    dispatcher.add_handler(unk_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
