from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    return render(request, 'utilities/index.html')


def artii(request):
   
    return render(request, 'utilities/artii.html')

def out_artii(request):

    name= request.GET.get('name')
    urls =f"http://artii.herokuapp.com/make?text={name}"
    print(urls)
    res = requests.get(urls)
    
    text=res.text

    context={
        'text': text,
    }
    return render(request, 'utilities/out_artii.html',context)
