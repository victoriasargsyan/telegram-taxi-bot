from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Укажите токен вашего бота
TOKEN = "7580087322:AAEbEk3UD6NKT3sjeuDhswehq1KvGwTElAI"

# Обработчики команд
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "👋 Привет! Добро пожаловать в наш сервис такси! 🚖\n"
        "Я помогу вам заказать такси. Используйте /order для начала.\n"
        "Если нужна помощь, напишите /help."
    )

async def order(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Введите ваш адрес и точку назначения.")

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Используйте команды:\n"
        "/start - начать работу с ботом\n"
        "/order - заказать такси\n"
        "/help - получить справку"
    )

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    await update.message.reply_text(f"Вы указали: {user_message}. Спасибо! Такси уже в пути.")

# Основная функция
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("order", order))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
