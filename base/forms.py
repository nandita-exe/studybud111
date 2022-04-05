from dataclasses import field
from django.forms import ModelForm,Textarea, TextInput
from .models import Room, User, Message
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username', 'email','password1','password2']

class RoomForms(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']



class UserForm(ModelForm):
    class Meta:
        model = User
        REQUIRED=['name','email']
        fields = ['avatar','name','username', 'email','bio']
        # widgets = {
        #     'name': Textarea(attrs={'class':'form-control', 'cols':'4','rows':'3','id':'exampleFormControlTextarea1','placeholder':'Username'}),
        #     'name': TextInput(attrs={'class':'form-control', 'id':'exampleFormControlTextarea1','placeholder':'Username'})
        # }



class UploadFileForm(ModelForm):
    class Meta:
        model = Message
        # REQUIRED=['name','email']
        fields = ['file']

# class MessageForm(ModelForm):