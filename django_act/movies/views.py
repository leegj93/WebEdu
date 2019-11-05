from django.shortcuts import render, redirect, HttpResponse
from .models import Movie
import pandas as pd

# Create your views here.

def index(request):
    movies = Movie.objects.all()

    context= {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method =="POST":
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience= request.POST.get('audience')
        open_date= request.POST.get('open_date')
        genre = request.POST.get('genre')
        print(genre)
        watch_grade= request.POST.get('watch_grade')
        score=request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        movie=Movie.objects.create(
            title= title, title_en= title_en, audience= audience, open_date= open_date, genre=genre, watch_grade=watch_grade, score=score, poster_url= poster_url, description= description )
        return redirect(movie)
    else:
        return render(request, 'movies/new.html')


def detail(request, movie_pk):
    movie= Movie.objects.get(pk=movie_pk)
    context={
        "movie":movie
    }
    return render(request,'movies/detail.html',context)




def load_data_csv(request):
    tmp_data= pd.read_csv('data.csv', sep=',')
    for i in range(len(tmp_data['title'])):
        tmp_data["open_date"][i]=pd.to_datetime(tmp_data['open_date'][i], format="%Y%m%d").date()
        print(type(tmp_data['open_date'][i]))
    for i in range(len(tmp_data['title'])):
         movies=[
            Movie(
                title=str(tmp_data['title'][i]),
                title_en=str(tmp_data['title_en'][i]),
                audience=int(tmp_data['audience'][i]),
                open_date=str(tmp_data['open_date'][i]),
                genre=str(tmp_data['genre'][i]),
                watch_grade=str(tmp_data['watch_grade'][i]),
                score=float(tmp_data['score'][i]),
                poster_url=str(tmp_data['poster_url'][i]),
                description=str(tmp_data['description'][i]),
        ).save(i)   
    ]
      

   
    return HttpResponse()


def update(request, movie_pk):
    movie =Movie.objects.get(pk=movie_pk)
    if request.method =="POST":
        title = request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience= request.POST.get('audience')
        open_date= request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade= request.POST.get('watch_grade')
        score=request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        movie=Movie.objects.create(
            title= title, title_en= title_en, audience= audience, open_date= open_date,
        genre=genre, watch_grade=watch_grade, score=score, poster_url= poster_url, description= description )
        return redirect(movie)
    else:
        return render(request, 'movies/update.html')

def delete(request, movie_pk):
    pass



        
