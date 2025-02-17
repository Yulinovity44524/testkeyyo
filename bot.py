from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /start, показывает меню выбора"""
    keyboard = [
        [InlineKeyboardButton("Pubg Mobile", callback_data='pubg_key')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет! Что хочешь выбрать:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    """Обработчик нажатий на кнопки"""
    query = update.callback_query
    query.answer()
    
    if query.data == 'pubg_key':
        query.edit_message_text(text="Ваш ключ: 576666-336-GA3Cq")

def main() -> None:
    """Запуск бота"""
    updater = Updater("7835506064:AAGyhtbS72oN0EyXfOI_HDNTaUtYb1pkrS8", use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
