from email.policy import default
from tkinter import Widget
from turtle import update
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.forms import PasswordInput

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True,blank=True,max_length=200)

    avatar = models.ImageField(null=True, default="avatar.svg")
    # password = models.CharField(models.widget=PasswordInput)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    link1 = models.CharField(max_length=250, blank=True)
    link2 = models.CharField(max_length=250, blank=True)
    link3 = models.CharField(max_length=250, blank=True)
    # link4 = models.
    def __str__(self):
        return self.name
        # return self.link

# class Link(models.Model):
#     topics = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
#     link = models.CharField(max_length=250, blank=True)

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # link = models.ForeignKey(Topic,to_field="link", db_column="link", on_delete=models.SET_NULL, null=True)
    # link = models.ManyToManyField(Topic, blank=True)
    name = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True, max_length=150)
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated', '-created']

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    file = models.FileField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # widget.attrs['class'] = 'someClass'
    class Meta:
        ordering = ['-updated', '-created']
    def __str__(self):
        return self.body[0:50]


