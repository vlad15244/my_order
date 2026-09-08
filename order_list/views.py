from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import OrdersSerializer
import json

# Create your views here.

from .models import Order, get_statuses_json
from .forms import OrderForm

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer

def orders_list(request):
    orders = Order.objects.order_by("-number")
    content = {"orders": orders}
    content["has_data"] = len(orders) > 0
    content["statuses"] = get_statuses_json(obj=Order.STATUS_ORDER)
    print(content)   

    return render(request, "order_list/orders_list.html", content)


def main(request):
    return redirect("orders/")

def add_order(request):

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_list")
    else:
        form = OrderForm()

    return render(request, "order_list/add.html", {"form": form})

def order_edit(request, number):

    order_instance = get_object_or_404(Order, number=number)

    if request.method == "POST":
        form = OrderForm(request.POST, order_instance)
        if format.is_valid():
            form.save()
            return redirect("order_list")
    else:
        form = OrderForm(instance=order_instance)
    return render(request, "order_list/edit.html", {"form": form})

@csrf_exempt
def sorted_orders(request):
    if request.method == "POST":
        body = json.loads(request.body)
        status_for_search = body.get("status")

        if status_for_search:


            if status_for_search == "all":
                query_set = Order.objects.all()
                content = list(query_set.values("id", "number", "equipment", "date"))
            else:
                query_set = Order.objects.filter(status=status_for_search)
                content = list(query_set.values("id", "number", "equipment", "date"))                
        else:
            query_set = Order.objects.all()
            content = list(query_set.values("id", "number", "equipment", "date"))
        return JsonResponse(
            {
                "status": status_for_search,
                "content": content,
                "has_data": len(query_set) > 0,
                "size": len(query_set),
            }
        )