from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def introduce(request, name,age):
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'pages/introduce.html',context)


def dinner(request):
    menu= ['짜장면', '햄버거', '치킨', '초밥', '김밥']
    pick = random.choice(menu)
    context= {'pick': pick}
    return render(request, 'pages/dinner.html',context)

def image(request):
    # image='https://picsum.photos/200/300'
    return render(request, 'pages/image.html')


def hello(request, name):
    menu= ['짜장면', '햄버거', '치킨', '초밥', '김밥']
    pick = random.choice(menu)
    context = {
        'name': name,
        'pick' : pick,
        }
    return render(request, 'pages/hello.html', context)
    

def times(request, num1, num2):
    result = num1*num2
    context={
        'num1':num1,
        'num2':num2,
        'result':result

    }
    return render(request, 'pages/times.html', context)

def circle(request, r):
    result = 3.14*r*r
    result=format(result,".2f")
    context={
        'r':r,
        'result':result
    }

    return render(request, 'pages/circle.html', context)


def template_language(request):
    menus=['짜장면', '햄버거', '치킨', '초밥', '김밥']
    my_sentence = "Life is short, you need python"
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow=datetime.now()
    empty_list=[]

    context={
        'menus':menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list':empty_list,

    }

    return render(request, 'pages/template_language.html', context)


def isbirth(request):
    today=datetime.today()
    if today.month == 10 and today.date== 8:
        result = True
    else:
        result = False
    
    context={
        'result':result
    }
    
    return render(request, 'pages/isbirth.html', context)


def ispal(request, word):
    if word == word[::-1]:
        result =True
    else:
        result = False
    context={
        'result': result,
        'word':word,
    }
    return render(request, 'pages/ispal.html',context)

