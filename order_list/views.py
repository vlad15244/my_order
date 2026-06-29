from django.shortcuts import render

# Create your views here.

from .models import Order


def orders_list(request):
    orders = Order.objects.order_by('-number') 
    content = {'orders' : orders}

    return render(request, 'order_list/orders_list.html', content)


