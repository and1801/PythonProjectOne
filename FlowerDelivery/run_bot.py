from telegram.ext import Updater
import logging
from django.conf import settings

def main():
    updater = Updater(token=settings.TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Включаем логирование
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    # Запуск бота
    updater.start_polling()
    print("Telegram-бот запущен!")
    updater.idle()

if __name__ == "__main__":
    import django
    django.setup()  # Инициализация Django
    main()