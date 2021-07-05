import random
import requests
from django.shortcuts import render, redirect
import time
from .forms import LocationForm
from .models import *
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import os
from django.urls import reverse
import datetime

class Weather:
    def __init__(self, temp, main, description, icon):
        self.temp = temp
        self.main = main
        self.description = description
        self.icon = icon


def get_weather(location):
    weather = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=0efdb2628f0f019f6151674dcc490192&units=metric").json()
    return weather

def get_forecast(lat, lon):
    weather = requests.get(k :=
        f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,hourly,minutely,alerts&appid=6471103eb1bc42bbd042e2b67531af1e&units=metric").json()
    return weather

@login_required
def index(request):
    return redirect("holiday_planner:all")

@login_required
def locations(request):
    favourites = request.user.favourite_set.all()
    favourite_locations = []
    for item in favourites:
        favourite_locations.append(item.location)
    search = ''
    user = request.user
    visits = user.visit_set.filter(user=user)
    visited_locations = []
    for loc in visits:
        visited_locations.append(loc.location)
    locations = Location.objects.all()
    items = []
    if request.method != 'POST':
        form = SearchForm()
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            search_locations = []
            search = form.cleaned_data['search']
            new_search_obj = Search(user=request.user, query=search)
            new_search_obj.save()
            locations = Location.objects.filter(city__icontains=search)
            for item in locations:
                search_locations.append(item)
            locations = Location.objects.filter(country__icontains=search)
            for item in locations:
                if item not in search_locations:
                    search_locations.append(item)
            locations = Location.objects.all()
            for location in locations:
                
                types = list(location.types.all())
                for item in types:
                    if str(item) == search:
                        search_locations.append(location)
            locations = search_locations
            if search.lower() == 'tim':
                locations = Location.objects.filter(country='Canada')
    for location in locations:
        location.description = location.description[:300]
        location.lat = 'aaa'
        if location in visited_locations:
            location.visited = True
        else:
            location.visited = False
        types = location.types.all()
        curitem = []
        curitem.append([str(type) for type in types])
        items.append(*curitem)
        location.tags = curitem

    return render(request, 'holiday_planner/locations.html', {"locations": locations, 'items': items, 'search': search, 'favourite_locations': favourite_locations, 'page': 'home'})


@login_required
def location(request, pk):
    favourites = request.user.favourite_set.all()
    
    
    location = Location.objects.get(pk=pk)
    for item in favourites:
        if location == item.location:
            location.fav = True
    new_search_obj = Search(user=request.user, query=location.city)
    new_search_obj.save()
    if request.method != 'POST':
        form = ReviewForm()
    else:
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            location.reviews += 1
            location.rating += int(int(form.cleaned_data['rating']) / location.reviews)
            new_review.user = request.user
            new_review.location = location
            new_review.save()
            location.save()
    weather = get_weather(location)
    if location.city.lower() == 'kutch':
        weather = get_weather('Bhuj')
    
    forecast = get_forecast(weather['coord']['lat'], weather['coord']['lon'])

    icons = []
    mins = []
    maxes = []
    descriptions = []
    for i in range(1, 8):
        w = forecast['daily'][i]
        mins.append(int(float(str(str(w['temp']['min'])))))
        maxes.append(int(float(str(str(w['temp']['max'])))))
        icons.append(w['weather'][0]['icon'])
        descriptions.append(w['weather'][0]['main'])
    days  = []
    curday = datetime.date.today()
    for i in range(7):
        curday += datetime.timedelta(1)
        days.append(curday.strftime("%A")[:3])
    if weather['cod'] == "404":
        weather = get_weather(location.country)
    try: 
        icon = weather["weather"][0]["icon"]
        temp =  weather['main']['temp']
        main = weather['weather'][0]['description']  
   
    except:
        weather = get_weather(location.country)
        icon = weather["weather"][0]["icon"]
        temp =  weather['main']['temp']
        main = weather['weather'][0]['description']
    maxlen = len(max(descriptions, key=len))
    descriptions = [(' ' * (maxlen - len(x))) + x for x in descriptions]
    location.google_maps = f'https://www.google.com/maps/place/{str(location)}'
    context = {"icons": icons, "maxes": maxes, "mins": mins, "main": main, "temp": temp, "icon": icon, "location": location, 'tags':
        location.types.all(), 'letters': [string for string in str(location).split(',')[0]], 'description': descriptions, "days": days}
    reviews = Review.objects.filter(location_id=pk)
    for review in reviews:
        review.nonrating = [i for i in range(5-review.rating)]
        review.rating = [i for i in range(review.rating)]
    context['reviews'] = reviews
    return render(request, 'holiday_planner/location.html', context)


def tag(request, tag):
    locations = Location.objects.filter()
    favourites = request.user.favourite_set.all()
    visited = request.user.visit_set.all()
    favourite_locations = []
    visited_locations = []
    for item in favourites:
        favourite_locations.append(item.location)
    for item in visited:
        visited_locations.append(item.location)
    tagged_locations = []
    tags = []
    for location in locations:
        curtags = []
        for item in location.types.all():
            if (str(item).lower()) == tag.lower():
                curtags.append([loc for loc in location.types.all()])
                tags.append(curtags)
                tagged_locations.append(location)
                continue
    print(tagged_locations)
    items = []
    for location in locations:
        types = location.types.all()
        curitem = []
        curitem.append([str(type) for type in types])
        items.append(curitem)
    return render(request, 'holiday_planner/tag.html', {'locations': tagged_locations, 'items': tags, 'tag': tag, 'fav': favourite_locations, "visited": visited_locations})

def post_review(request, pk):
    location = Location.objects.get(pk=pk)
    return render(request, 'holiday_planner/')


def query(request):
    if request.method != 'POST':
        form = QueryForm()
    else:
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query.lower() == 'Tim':
                print('timmy')
                locations.append(Location.objects.filter(country='Canada'))

        locations.append(Location.objects.filter(city__unaccent__icontains=str(query)))
    return render(request, 'holiday_planner/query.html', {"locations": locations})

@login_required
def handle_visit(request, pk):
    new_visit_obj = Visit(user=request.user,    location=Location.objects.get(pk=pk))
    try:
        old_objs = Visit.objects.get(user=request.user, location=Location.objects.get(pk=pk))
        old_objs.delete()
        return JsonResponse({"type": '1'}) 
    except:
        new_visit_obj = Visit(user=request.user,    location=Location.objects.get(pk=pk))
        new_visit_obj.save()
        print('yeah')
        return JsonResponse({"type": '2'}) 
    


def remove_visit(request, pk):
    visit = Visit.objects.get(user=request.user, location=Location.objects.get(pk=pk))
    visit.delete()
    return JsonResponse({"status": 'Success'}) 


def delete_review(request, pk):
    review = Review.objects.get(id=pk)
    review.delete()
    return JsonResponse({'status': 'success'})

def favourite(request, pk):
    try:
        new_search_obj = Favourite.objects.get(user=request.user, location=Location.objects.get(pk=pk))
        new_search_obj.delete()
        return JsonResponse({'message': 'success', 'type': 1})
    except Exception as e:
        print(e)
        new_favourite_obj = Favourite(user=request.user, location=Location.objects.get(pk=pk))
        new_favourite_obj.save()
        return JsonResponse({'message': 'success', 'type': 2})

def email(request):
    if request.method != 'POST':
        form = EmailForm()
    else:
        form = EmailForm(request.POST)
        print('ye')
        if form.is_valid():
            print('yes')
            form.save()
            
    return JsonResponse({"message": "success"})
