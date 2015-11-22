from django import forms

class form1(forms.Form):
    name=forms.CharField()
    year=forms.IntegerField()
    branch=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()
    usertype=forms.CharField()
    