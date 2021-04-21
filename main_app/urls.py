from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # pedals routes
    path('pedals/', views.pedals_index, name='index'),
    path('pedals/<int:pedal_id>/', views.pedals_detail, name='detail'),
    path('pedals/create/', views.PedalCreate.as_view(), name='pedals_create'),
    path('pedals/<int:pk>/update/', views.PedalUpdate.as_view(), name='pedals_update'),
    path('pedals/<int:pk>/delete/', views.PedalDelete.as_view(), name='pedals_delete'),
    path('pedals/<int:pedal_id>/add_knob/', views.add_knob, name='add_knob'),
    path('pedals/<int:pedal_id>/assoc_guitar/<int:guitar_id>/', views.assoc_guitar, name='assoc_guitar'),

    # guitars routes
    path('guitars/', views.guitars_index, name='all_guitars'),
    path('guitars/<int:guitar_id>/', views.guitar_detail, name='guitar_detail'),
    path('guitars/create/', views.Create_Guitar.as_view(), name='create_guitar'),
    path('guitars/<int:pk>/update/', views.Update_guitar.as_view(), name='update_guitar'),
    path('guitars/<int:pk>/delete/', views.Delete_guitar.as_view(), name='delete_guitar'),
]