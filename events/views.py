from django.shortcuts import render

# Create your views here.

from .models import Event

def events_list(request):
    events = Event.objects.order_by('-date') 
    content = {'events' : events}
    content['has_data'] = len(events) > 0

    return render(request, 'events/events_list.html', content)
