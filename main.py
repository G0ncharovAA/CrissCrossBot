from secret import API_KEY
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
import game

counter = 0
tokens = [chr(10060), chr(11093)]


def start(update: Update, context: CallbackContext) -> int:
    global counter
    counter = 0
    game.reset()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=game.draw_board())
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Enter a number from 1 to 9.\nSelect a position {tokens[counter % 2]}? ")
    return 0


def turn(update: Update, context: CallbackContext) -> int:
    global counter
    position = update.message.text
    response = game.place_sign(counter % 2, position)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=response)
    if response == "ok":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=game.draw_board())
        counter += 1
        if counter > 3:
            if game.check_win():
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=f"{game.check_win()} - WIN{chr(127942)}{chr(127881)}!")
                game.reset()
                counter = 0
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=game.draw_board())
        if counter == 8:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"Draw game {chr(129318)}{chr(129309)}")
            game.reset()
            counter = 0
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=game.draw_board())
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Enter a number from 1 to 9.\nSelect a position {tokens[counter % 2]}? ")
    return 0


def cancel(update: Update, context: CallbackContext) -> int:
    return ConversationHandler.END


def main():
    updater = Updater(API_KEY)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            0: [MessageHandler(Filters.all, turn)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
