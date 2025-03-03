from telegram import Bot
from django.conf import settings

# Инициализация бота
bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

def send_order_notification(order):
    """
    Отправляет уведомление о новом заказе в Telegram.
    """
    # Формируем текст сообщения
    message = (
        f"🔔 Новый заказ! 🔔\n"
        f"ID заказа: {order.id}\n"
        f"Пользователь: {order.user.username}\n"
        f"Дата доставки: {order.delivery_date}\n"
        f"Время доставки: {order.delivery_time}\n"
        f"Адрес: {order.address}\n"
        f"Комментарий: {order.comment or 'Нет комментария'}\n"
        f"Товары:\n"
    )

    # Добавляем информацию о товарах
    for item in order.orderitem_set.all():
        message += (
            f"- {item.product.name} (x{item.quantity}) - ${item.product.price * item.quantity}\n"
        )

    # Общая стоимость заказа
    total_price = sum(item.product.price * item.quantity for item in order.orderitem_set.all())
    message += f"\nОбщая стоимость: ${total_price}"

    # Отправляем сообщение в Telegram
    try:
        bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)
    except Exception as e:
        print(f"Ошибка при отправке уведомления в Telegram: {e}")