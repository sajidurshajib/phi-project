from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('about/background', views.about_background, name='about-background'),
    path('about/history', views.about_history, name='about-history'),
    path('about/partners', views.about_partners, name='about-partners'),
    path('programs/survillance', views.programs_surveillance, name='programs-survillance'),
    path('programs/emergency', views.programs_emergency, name='programs-emergency'),
    path('programs/lab', views.programs_lab, name='programs-lab'),
    path('programs/workforce', views.programs_workforce, name='programs-workforce'),
]