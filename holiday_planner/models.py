import time

from django.db import models
from django.contrib.auth.models import User


class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.CharField(max_length=1000, unique=True)
    rating = models.FloatField(default=0, null=True, blank=True)
    reviews = models.IntegerField(default=0)
    country = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=2083, unique=True)
    types = models.ManyToManyField(Type)
    description = models.TextField(default='', unique=True)

    def __str__(self):
        return f"{self.city}, {self.country}"

class Review(models.Model):
    title = models.CharField(max_length=800)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}, {self.location}"

class Search(models.Model):
    query = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'searches'
    
    def __str__(self):
        return f"{self.query} -> {self.user}"

class Favourite(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()
