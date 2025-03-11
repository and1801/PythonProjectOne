from django.shortcuts import render, redirect
from .models import Order, OrderItem
from products.models import Product
from .forms import OrderForm
from django.contrib import messages
from .bot import send_order_notification
import asyncio



def clear_cart(request):
    request.session['cart'] = {}  # Очищаем корзину
    return redirect('view_cart')

def order_confirmation(request):
    return render(request, 'orders/order_confirmation.html')

def view_cart(request):
    cart = request.session.get('cart', {})  # Получаем корзину из сессии
    cart_items = []

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity,
        })

    total_cart_price = sum(item['total_price'] for item in cart_items)

    return render(request, 'orders/cart.html', {
        'cart_items': cart_items,
        'total_cart_price': total_cart_price,
    })

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('catalog')

def checkout(request):
    if request.method == 'POST':
        # Получаем данные из формы
        user = request.user
        delivery_date = request.POST.get('delivery_date')
        delivery_time = request.POST.get('delivery_time')
        address = request.POST.get('address')
        comment = request.POST.get('comment')

        # Создаем заказ
        order = Order.objects.create(
            user=user,
            delivery_date=delivery_date,
            delivery_time=delivery_time,
            comment=comment,
            address=address
        )

        # Добавляем товары из корзины в заказ
        cart = request.session.get('cart', {})
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        # Очищаем корзину
        request.session['cart'] = {}

        # Отправляем уведомление в Telegram
        try:
            send_order_notification(order)
        except Exception as e:
            messages.error(request, f'Ошибка: {str(e)}')



        # Перенаправляем на страницу успешного оформления заказа
        return redirect('order_success')

    return render(request, 'orders/checkout.html')