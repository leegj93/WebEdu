from django.shortcuts import render
from decouple import config
from faker import Faker
from .models import Job
import requests

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    name = request.POST.get("name")

    # db에 이름이 있는지 확인
    person = Job.objects.filter(name=name).first()
    
    # db에 이미 같은 name이 있으면 기존 name의 past_job 가져오기
    if person:
        past_job = person.past_job

    # 없으면 db에 저장한 후 가져오기
    else:
        faker = Faker()
        past_job = faker.job()
        person = Job(name=name, past_job=past_job)
        person.save()

    GIPHY_API_KEY = config("GIPHY_API_KEY")
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}'
    data = requests.get(url).json()
    image = data.get("data")[0].get("images").get("original").get("url")
    # image = data["data"][0]["images"]["original"]["url"]

    context = {'person': person, 'image': image}
    return render(request, 'jobs/past_life.html', context)