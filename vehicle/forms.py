from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from vehicle.models import Vehicles
from tkinter import Widget

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
                "first_name",
                "last_name",
                "username",
                "email",
                "password1",
                "password2",
                
                ]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

# my_choices=[("2","two"),("3","three"),("4","four")]

# class VehicleForm(forms.Form):
#     name=forms.CharField(label="name",required=True)
#     number=forms.CharField(label="number",required=True)
#     type=forms.NumberInput(label="type",required=True)
#     model=forms.CharField(label="model",required=True)
#     description=forms.CharField(label="description",required=True)






class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields=[
            "name","number","type","model","description"
        ]
        widgets={
            "name":forms.Textarea(attrs={"class":"form-control","rows":2}),
            "number":forms.Textarea(attrs={"class":"form-control","rows":1}),
            "type":forms.TextInput(attrs={"class":"form-control"}),
            "model":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control","rows":3})
        }