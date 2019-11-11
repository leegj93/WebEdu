from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.http import Http404

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context={'articles': articles}
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method=="POST":
        # 폼 인스턴스를 생성하고 요청에 의한 데이터로 채운다
        form =ArticleForm(request.POST)
        # 폼이 유효한지 체크한다.
        if form.is_valid():
            title=form.cleaned_data.get('title')
            content= form.cleaned_data.get('content')
            article=Article(title=title, content=content)
            article.save()
    # if request.method=="POST":
    #     title = request.POST.get('title')
    #     content= request.POST.get('content')
    #     article=Article(title=title, content=content)
    #     article.save()
        return redirect('articles:index')
    else:
        form= ArticleForm()
        context={'form': form}
    return render(request, 'articles/create.html',context)


def detail(request, article_pk):
    # article= Article.objects.get(pk=article_pk)
    article=get_object_or_404(Article, pk=article_pk)
    try:
        article=Article.objects.get(pk=article_pk)
    except Article.DoesNotExist:
        raise Http404("No article matches the given query")
    context={'article':article}
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article=get_object_or_404(Article, pk=article_pk)
    if request.method=='POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article_pk)