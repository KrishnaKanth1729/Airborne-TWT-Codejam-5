from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from holiday_planner.models import *

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
# View to save new users to database

>>>>>>> a3a932dce409083a7c6e35af7d3c9bcb24f84cc5
>>>>>>> 718c113696141d4fb8baffc1116040e0e814cf51

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('holiday_planner:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
# View for the Profile Page which displays all the user information.
>>>>>>> a3a932dce409083a7c6e35af7d3c9bcb24f84cc5
>>>>>>> 718c113696141d4fb8baffc1116040e0e814cf51
@login_required
def profile(request):
    context = {}
    visited_locations = []
    reviews = request.user.review_set.all()
    visited = request.user.visit_set.all()
    searched = request.user.search_set.all()
    liked = request.user.favourite_set.all()
    liked_locations = []
    for item in liked:
        liked_locations.append(item.location)
    for review in reviews:
        review.nonrating = [i for i in range(5-review.rating)]
        review.rating = [i for i in range(review.rating)]
<<<<<<< HEAD
        
=======
<<<<<<< HEAD
        
=======

>>>>>>> a3a932dce409083a7c6e35af7d3c9bcb24f84cc5
>>>>>>> 718c113696141d4fb8baffc1116040e0e814cf51
    for location in visited:
        visited_locations.append(location.location)
    context['locations'] = visited_locations
    context['search'] = list(searched)[::-1][:10]
    context['reviews'] = reviews
    context['liked'] = liked_locations
    return render(request, 'registration/profile.html', context)
