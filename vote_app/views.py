from django.shortcuts import render
import requests
# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request,'home.html', {'name':'Deepta'})

def candidate_list(request):
    response = requests.get('https://api.covid19api.com/countries').json()
    return render(request,'candidate_list.html', {'response': response})

def vote_candidate(request):
    return render(request,'vote_page.html', {})

def votingAction(request):
    candidate_id = request.POST.get("candidate_id")
    constituency_id = request.POST.get('constituency_id')
    post_data = {'candidate_id':candidate_id, 'constituency_id':constituency_id }
    # api_response = requests.post(url = "api_endpoint", data = post_data )
    return render(request, 'vote_confirm.html',post_data)

# {'candidate_id': candidate_id, 'constituency_id': constituency_id}