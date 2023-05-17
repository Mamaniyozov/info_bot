from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
import telegram
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os
# from db import DB
# from cartdb import Cart
# get token from env
TOKEN = os.environ['TOKEN']
path= os.getcwd()
def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    
    keyboar = ReplyKeyboardMarkup([
        ['📝 About you']
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )
def About(update: Update, context: CallbackContext):
        chat_id = update.message.chat.id
        keyboar = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='📞 Phone number',callback_data='number'),InlineKeyboardButton(text='📧 Email',callback_data='email')],
        [InlineKeyboardButton(text='📍 Location',callback_data='location'),InlineKeyboardButton(text='📌 Address',callback_data='address')],
        ])
        bot = context.bot
        bot.sendMessage(
        chat_id=chat_id,
        text='Assalom alaykum xush kelibsiz botimizga 👍',
        reply_markup=keyboar
        )
        
def query(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    data = query.data
    bot = context.bot
    if data=='number':
        text = "Telefon raqamingizni kiriting"
        reply_markup = telegram.ReplyKeyboardMarkup([[telegram.KeyboardButton('Share contact', request_contact=True)]])

        bot.sendMessage(chat_id, 'Example', reply_markup=reply_markup)
        bot.sendMessage(text=text,chat_id=chat_id)
    elif data=='email':
        email = 'Our email: smartphone@gmail.com'
        bot.sendMessage(text=email,chat_id=chat_id)
        
    elif data=='address':
        address = 'Our address: Samarkand, Uzbekistan'
        bot.sendMessage(text=address,chat_id=chat_id)

    elif data=='location':
        # 39.644053, 66.973233

        lat = 39.644053
        lon = 66.973233
        bot.sendLocation(chat_id=chat_id,latitude=lat,longitude=lon)

    query.answer('Hi')
    print(data)
    
def main():              
    updater = Updater(token=TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start',start))
    # Add handler for photo message
    updater.dispatcher.add_handler(MessageHandler(Filters.text('📝 About you'),About))
    updater.dispatcher.add_handler(MessageHandler(Filters.text('Main menu'),start))
    
    updater.dispatcher.add_handler(CallbackQueryHandler(query))

    updater.start_polling()
    updater.idle()
    