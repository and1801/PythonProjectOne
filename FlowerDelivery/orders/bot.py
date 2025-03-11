# orders/bot.py

from telegram import Bot
from django.conf import settings
import requests


def send_order_notification(order):
    message = (
        f"🔔 Новый заказ! 🔔\n"
        f"ID: {order.id}\n"
        f"Пользователь: {order.user.username}\n"
        f"Адрес: {order.address}\n"
        f"Дата/время: {order.delivery_date} {order.delivery_time}\n"
        f"Комментарий: {order.comment or 'Нет'}\n"
        f"Товары:\n"
    )

    # Синхронно получаем товары
    for item in order.orderitem_set.all():
        message += f"- {item.product.name} (x{item.quantity}) - ${item.product.price * item.quantity}\n"

    total_price = sum(item.product.price * item.quantity for item in order.orderitem_set.all())
    message += f"\nОбщая стоимость: ${total_price}"

    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': settings.TELEGRAM_CHAT_ID,
        'text': message
    }

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Проверка HTTP-ошибок
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке уведомления: {e}")