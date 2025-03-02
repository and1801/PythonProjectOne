from django.shortcuts import render
from .models import Product
from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/catalog.html'  # Указываем путь к шаблону
    context_object_name = 'products'

def catalog(request):
    products = Product.objects.all()
    return render(request, 'products/catalog.html', {'products': products})

# Create your views here.
