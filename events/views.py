from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
# Create your views here.

from .models import Event
from .forms import EventForm
from order_list.models import get_statuses_json, Order


def events_list(request):
    events = Event.objects.order_by('-date')
    content = {'events': events}
    content['has_data'] = len(events) > 0
    content['statuses'] = get_statuses_json(obj=Event.CLASS_EVENT)
    content['orders'] = Order.objects.order_by('-date')

    return render(request, 'events/events_list.html', content)


def add_order(request):

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("events_list")
    else:
        form = EventForm()

    return render(request, "events/add.html", {"form": form})

@csrf_exempt
def sorted_orders(request):
    if request.method == "POST":
        body = json.loads(request.body)
        order_for_search = body.get("order")

        if order_for_search:

            if order_for_search == "all":
                query_set = Order.objects.all()
                content = list(query_set.values("id", "number", "equipment", "date"))
            else:
                query_set = Order.objects.filter(status=order_for_search)
                content = list(query_set.values("id", "number", "equipment", "date"))                
        else:
            query_set = Order.objects.all()
            content = list(query_set.values("id", "number", "equipment", "date"))
        return JsonResponse(
            {
                "status": order_for_search,
                "content": content,
                "has_data": len(query_set) > 0,
                "size": len(query_set),
            }
        )
