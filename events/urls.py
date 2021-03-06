from django.urls import path
from . import views


urlpatterns = [
    path('<int:year>/<str:month>/', views.home, name='events'),
    path('events/', views.all_events, name='list-events'),
    path('add_venue', views.add_venue, name='add-venue'),
    path('list_venues', views.list_venues, name='list-venues'),
    path('search_venues', views.search_venues, name='search-venues'),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete-venue'),
    path('delete_event/<event_id>', views.delete_event, name='delete-event'),
    path('my_venues>', views.my_venues, name='my-venues'),
]