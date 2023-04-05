from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm


class CalendarView(generic.ListView):
    model = Event
    template_name = 'events/calendar.html'


class EventCreateView(generic.CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('calendar')
    template_name = 'events/event_form.html'


def calendar(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
    else:
        form = EventForm()
    return render(request, 'events/calendar.html', {'form': form})


def home(request):
    return render(request, 'events/home.html')