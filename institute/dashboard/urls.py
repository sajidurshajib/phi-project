from django.urls import path
from . import views
from events.views import events, events_add, events_edit, events_remove

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='dashboard-profile'),
    
    path('events/', events, name='dashboard-events'),
    path('events-add/', events_add, name='dashboard-events-add'),
    path('events-edit/<int:id>', events_edit, name='dashboard-events-edit'),
    path('events-remove/<int:id>', events_remove, name='dashboard-events-remove'),
]