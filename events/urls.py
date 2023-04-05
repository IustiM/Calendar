from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.EventCreateView.as_view(), name='event_create'),
]
