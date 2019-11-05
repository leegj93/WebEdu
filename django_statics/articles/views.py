from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    articles= Article.objects.all()
    context={
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_pk):
    article= Article.objects.get(pk=article_pk)
    context={
        'article' : article
    }
    return render(request, 'articles/detail.html',context)
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method== "POST":
        article.title= request.POST.get('title')
        article.content=request.POST.get('content')
        article.image=request.FILES.get('image')
        article.save()
        # article = Article.objects.get(pk=article_pk)
        return redirect('articles:detail', article_pk)
    else:
        context={'article': article}
        return render(request, 'articles/update.html',context)
    


def create(request):
    if request.method=="POST":
        title= request.POST.get('title')
        content = request.POST.get('content')
        image= request.FILES.get('image')
        article= Article(
            title=title,
            content=content,
            image=image
        )
        article.save()
        return redirect("articles:index")
    else:
        return render(request, 'articles/create.html')


def delete(request, article_pk):
    article= Article.objects.get(pk=article_pk)
    article.image.delete()
    article.delete()
    return redirect('articles:index')