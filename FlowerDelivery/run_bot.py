import logging
from telegram.ext import ApplicationBuilder, CommandHandler
import os
import django

# Установка переменной окружения для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FlowerDelivery.settings')
django.setup()

# Импорт после инициализации Django
from django.conf import settings
from telegram import Bot
from orders.bot import send_order_notification  # Импортируем вашу функцию уведомлений

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Инициализация бота
bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)


async def start(update, context):
    await update.message.reply_text("Привет! Я бот для уведомлений о заказах.")


def main():
    # Создаем приложение
    application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

    # Регистрируем команду /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()
    print("Telegram-бот запущен!")


if __name__ == "__main__":
    main()