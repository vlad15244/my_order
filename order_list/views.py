from django.shortcuts import render, redirect

# Create your views here.

from .models import Order
from .forms import OrderForm


def orders_list(request):
    orders = Order.objects.order_by('-number') 
    content = {'orders' : orders}

    return render(request, 'order_list/orders_list.html', content)

def add_order(request):

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()

    return render(request, 'order_list/add.html', {'form': form})


