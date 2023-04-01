from django.shortcuts import render
import requests
# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request,'home.html', {'name':'Deepta'})

def candidate_list(request):
    response = requests.get('https://api.covid19api.com/countries').json()
    return render(request,'candidate_list.html', {'response': response})