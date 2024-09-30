from django.urls import path
from . import views
from managements.views import managements, managements_add, managements_edit, managements_remove
from resources.views import resources, resources_add, resources_edit, resources_remove
from events.views import events, events_add, events_edit, events_remove

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='dashboard-profile'),

    path('managements/', managements, name='dashboard-managements'),
    path('managements-add/', managements_add, name='dashboard-managements-add'),
    path('managements-edit/<int:id>', managements_edit, name='dashboard-managements-edit'),
    path('managements-remove/<int:id>', managements_remove, name='dashboard-managements-remove'),

    path('resources/', resources, name='dashboard-resources'),
    path('resources-add/', resources_add, name='dashboard-resources-add'),
    path('resources-edit/<int:id>', resources_edit, name='dashboard-events-edit'),
    path('resources-remove/<int:id>', resources_remove, name='dashboard-resources-remove'),

    path('events/', events, name='dashboard-events'),
    path('events-add/', events_add, name='dashboard-events-add'),
    path('events-edit/<int:id>', events_edit, name='dashboard-events-edit'),
    path('events-remove/<int:id>', events_remove, name='dashboard-events-remove'),
]