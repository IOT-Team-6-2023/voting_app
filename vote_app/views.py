from django.shortcuts import render
import requests
# Create your views here.

from django.http import HttpResponse

BASE = "http://192.168.196.59:3000"


def index(request):
    return render(request,'home.html')

def candidate_list(request):
    api_end_point = BASE + "/candidates"
    response = requests.get(api_end_point).json()
    return render(request,'candidate_list.html', {'response': response})

def vote_candidate(request):
    return render(request,'vote_page.html', {})

def votingAction(request):
    candidate_id = request.POST.get("candidate_id")
    post_data = {'candidate_id':candidate_id }
    api_response = requests.post(url = BASE +"/votes", json = post_data )
    print(api_response)
    return render(request, 'vote_confirm.html',post_data)
