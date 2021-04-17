from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pedals/', views.pedals_index, name='index'),
    path('pedals/<int:pedal_id>/', views.pedals_detail, name='detail'),
    path('pedals/create/', views.PedalCreate.as_view(), name='pedals_create'),
    path('pedals/<int:pk>/update/', views.PedalUpdate.as_view(), name='pedals_update'),
path('pedals/<int:pk>/delete/', views.PedalDelete.as_view(), name='pedals_delete'),
]