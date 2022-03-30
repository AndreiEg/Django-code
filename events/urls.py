from django.urls import path
from . import views


urlpatterns = [
    path('<int:year>/<str:month>/', views.home, name='events'),
    path('events/', views.all_events, name='list-events'),
    path('add_venue', views.add_venue, name='add-venue'),
]