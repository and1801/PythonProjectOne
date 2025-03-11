import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import django
from telegram import Bot
from django.conf import settings
import asyncio
import requests
import aiohttp



# Инициализация Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FlowerDelivery.settings')
django.setup()

# Импортируем настройки Django
from django.conf import settings

# Определяем команду /start для тестирования бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Привет! Я бот для уведомлений о заказах.")

logger = logging.getLogger(__name__)

def main():
    # Создаем приложение с использованием токена
    application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Настройка логирования
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    # Запуск бота
    application.run_polling()
    print("Telegram-бот запущен!")



async def send_order_notification(order):
    bot_token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    message = f"Новый заказ #{order.id} от {order.user.username}"

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': message}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload) as response:
            print(f"Ответ Telegram API: {response.status}, {await response.text()}")


# async def send_order_notification(order):
#     """
#     Отправляет уведомление о новом заказе в Telegram.
#     """
#     bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
#     message = (
#         f"🔔 Новый заказ! 🔔\n"
#         f"ID заказа: {order.id}\n"
#         f"Пользователь: {order.user.username}\n"
#         f"Дата доставки: {order.delivery_date}\n"
#         f"Время доставки: {order.delivery_time}\n"
#         f"Адрес доставки: {order.address or 'Не указан'}\n"
#         f"Комментарий: {order.comment or 'Нет комментария'}\n"
#         f"Товары:\n"
#     )
#
#     for item in order.orderitem_set.all():
#         message += (
#             f"- {item.product.name} (x{item.quantity}) - ${item.product.price * item.quantity}\n"
#         )
#     total_price = sum(item.product.price * item.quantity for item in order.orderitem_set.all())
#     message += f"\nОбщая стоимость: ${total_price}"
#
#     try:
#         await bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)  # Используем await
#     except Exception as e:
#         logger.error(f"Ошибка при отправке уведомления: {e}")
#         raise

# def send_order_notification(order):
    # """
    # Отправляет уведомление о новом заказе в Telegram через синхронный HTTP API.
    # """
    # bot_token = settings.TELEGRAM_BOT_TOKEN
    # chat_id = settings.TELEGRAM_CHAT_ID
    # message = (
    #     f"🔔 Новый заказ! 🔔\n"
    #     f"ID заказа: {order.id}\n"
    #     f"Пользователь: {order.user.username}\n"
    #     f"Дата доставки: {order.delivery_date}\n"
    #     f"Время доставки: {order.delivery_time}\n"
    #     f"Адрес доставки: {order.address or 'Не указан'}\n"
    #     f"Комментарий: {order.comment or 'Нет комментария'}\n"
    #     f"Товары:\n"
    # )
    # for item in order.orderitem_set.all():
    #     message += (
    #         f"- {item.product.name} (x{item.quantity}) - ${item.product.price * item.quantity}\n"
    #     )
    # total_price = sum(item.product.price * item.quantity for item in order.orderitem_set.all())
    # message += f"\nОбщая стоимость: ${total_price}"
    #
    # url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # payload = {
    #     'chat_id': chat_id,
    #     'text': message
    # }
    # try:
    #     response = requests.post(url, data=payload)
    #     response.raise_for_status()  # Проверка на ошибки HTTP
    # except Exception as e:
    #     print(f"Ошибка при отправке уведомления: {e}")




    # bot_token = settings.TELEGRAM_BOT_TOKEN
    # chat_id = settings.TELEGRAM_CHAT_ID
    # message = f"Новый заказ #{order.id} от {order.user.username}"
    #
    # url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    # payload = {
    #     'chat_id': chat_id,
    #     'text': message
    # }
    #
    # try:
    #     response = requests.post(url, data=payload)
    #     response.raise_for_status()  # Проверка HTTP-ошибок
    # except requests.exceptions.RequestException as e:
    #     print(f"Ошибка отправки: {e}")




if __name__ == "__main__":
    main()