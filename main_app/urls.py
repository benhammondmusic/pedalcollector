from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pedals/', views.pedals_index, name='index'),
    path('pedals/<int:pedal_id>/', views.pedals_detail, name='detail')
    
]