from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event
from django.contrib.auth.models import Group


admin.site.register(MyClubUser)
admin.site.unregister(Group)


@admin.register(Venue)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone','approved')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('name',)