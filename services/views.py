from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'services/index.html')

def artii(request):
    return render(request, 'services/artii.html')

def artii_result(request):
    word = request.GET.get('word')
    font = request.GET.get('font')
    result = requests.get('http://artii.herokuapp.com/make?text={}&font={}'.format(word,font))
    context = {
        'result' : result.text
    }
    return render(request, 'services/artii_result.html', context)

def workshop(request):
    return render(request, 'services/workshop.html')

def workshop_result(request):
    number = request.GET.get('number')
    context = {
        'number': number
    }
    return render(request, 'services/workshop_result.html', context)