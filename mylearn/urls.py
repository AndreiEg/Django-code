import django.contrib.auth.urls
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('', include('members.urls')),
    path('', include('main.urls')),
]
admin.site.site_header = "My Site Administration Page"
admin.site.site_title = 'Browser Title'
admin.site.index = "Welcome to admin area"