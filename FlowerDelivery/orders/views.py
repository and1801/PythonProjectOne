from django.shortcuts import render, redirect
from .models import Order, OrderItem
from products.models import Product
from .forms import OrderForm
from django.contrib import messages
from .bot import send_order_notification

def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            delivery_date = form.cleaned_data['delivery_date']
            delivery_time = form.cleaned_data['delivery_time']
            comment = form.cleaned_data['comment']

            # Создаем заказ
            user = request.user
            order = Order.objects.create(
                user=user,
                delivery_date=delivery_date,
                delivery_time=delivery_time,
                comment=comment,
                status='new'
            )

            # Добавляем товары из корзины в заказ
            cart = request.session.get('cart', {})
            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity
                )

            # Очищаем корзину
            request.session['cart'] = {}

            # Отправляем уведомление в Telegram
            send_order_notification(order)

            # Показываем сообщение об успехе
            messages.success(request, 'Заказ успешно оформлен!')
            return redirect('order_confirmation')
    else:
        form = OrderForm()

    return render(request, 'orders/checkout.html', {'form': form})
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
        user = request.user
        delivery_date = request.POST.get('delivery_date')
        delivery_time = request.POST.get('delivery_time')
        comment = request.POST.get('comment')

        order = Order.objects.create(
            user=user,
            delivery_date=delivery_date,
            delivery_time=delivery_time,
            comment=comment
        )

        cart = request.session.get('cart', {})
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        request.session['cart'] = {}
        return redirect('order_success')

    return render(request, 'orders/checkout.html')