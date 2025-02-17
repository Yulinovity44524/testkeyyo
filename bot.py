from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Токен вашего бота
TOKEN = '7835506064:AAGyhtbS72oN0EyXfOI_HDNTaUtYb1pkrS8'

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Создаем клавиатуру с кнопками
    keyboard = [['Кнопка 1', 'Кнопка 2'], ['Кнопка 3', 'Кнопка 4']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    
    # Отправляем сообщение с клавиатурой
    await update.message.reply_text('Выберите одну из кнопок:', reply_markup=reply_markup)

# Функция для обработки текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f'Вы выбрали: {text}')

def main():
    # Создаем приложение и передаем токен
    application = Application.builder().token(TOKEN).build()
    
    # Регистрируем обработчики команд и сообщений
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()