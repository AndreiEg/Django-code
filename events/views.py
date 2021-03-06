from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, VenueFormAdmin
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib import messages


def my_venues(request):
    if request.user.is_authenticated:
        me = request.user.id
        venues = Venue.objects.filter(owner=me)
        return render(request, 'events/my_venues.html', {
            'venues': venues
        })
    else:
        return redirect('add-venue')


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    if request.user.is_superuser:
        venue.delete()
        messages.success(request,('Venue is deleted'))
        return redirect('list-venues')
    else:
        messages.success(request, ('You are not admin'))
        return redirect('list-venues')


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user.is_superuser:
        form = VenueFormAdmin(request.POST or None, instance=event)
    else:
        form = VenueForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/update_event.html', {'event': event, 'form': form})


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    if request.user.is_superuser:
        form = VenueFormAdmin(request.POST or None, request.FILES or None, instance=venue)
    else:
        form = VenueForm(request.POST or None, request.FILES or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    return render(request, 'events/update_venue.html', {'venue': venue, 'form': form})


def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search_venues.html', {})


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/venue.html', {'venue': venue})


def list_venues(request):
    venue_list = Venue.objects.all()
    p = Paginator(Venue.objects.all(), 1)
    page = request.GET.get('page')
    venues = p.get_page(page)
    return render(request, 'events/venues.html', {
        'venue_list': venue_list,
        'venues': venues,
    })


def add_venue(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = VenueFormAdmin(request.POST, request.FILES)
        else:
            form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner = request.user.id
            venue.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        if request.user.is_superuser:
            form = VenueFormAdmin
        else:
            form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {
        'event_list': event_list
    })


def home(requests, year, month):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )
    now = datetime.now()
    current_year = now.year
    return render(requests, 'events/events.html', {
        'year': year,
        'month_number': month_number,
        'cal': cal,
        'current_year': current_year
    })
