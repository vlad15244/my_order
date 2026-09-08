from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

from .models import Event
from .forms import EventForm
from order_list.models import get_statuses_json


def events_list(request):
    events = Event.objects.order_by('-date')
    content = {'events': events}
    content['has_data'] = len(events) > 0
    content['statuses'] = get_statuses_json(obj=Event.CLASS_EVENT)

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
