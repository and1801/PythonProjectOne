from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Маршрут для добавления в корзину
    path('cart/', views.view_cart, name='view_cart'),  # Маршрут для страницы корзины
    path('cart/clear/', views.clear_cart, name='clear_cart'),
    path('checkout/', views.checkout, name='checkout'),  # Маршрут для оформления заказа
    path('order_success/', views.order_confirmation, name='order_success'),  # Новый маршрут
]