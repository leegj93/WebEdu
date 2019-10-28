from django.shortcuts import render
import random
import requests
# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def throw(request):
    return render(request, 'pages/throw.html')


def catch(request):
    
    message =request.GET.get("message")
    message2= request.GET.get("message2")
    context= {
        'message': message,
        'message2': message2,
    }
    return render(request, 'pages/catch.html', context)


def lotto_pick(request):
    return render(request, 'pages/lotto_pick.html')

def lotto_get(request):
    lottos= range(1,46)
    pick = random.sample(lottos, 6)
    name = request.GET.get('name')

    context={
        'name': name,
        'pick': pick
    }
    return render(request, 'pages/lotto_get.html', context)

def lottery(request):
    return render(request, 'pages/lottery.html')
    

def jackpot(request):
    # 1. 사용자의 이름을 받아오자
    name=request.GET.get('name')
    # 2. 로또 홈페이지 개발자 도구 network xhr 클릭
    # Header에 Request url 과 drwNo의 정보를 알아야함
    # 최종 url https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=882

    res= requests.get("https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=882")
    res=res.json()
    # print(res.get('drwtNo6'))
    # 3. 로또 당첨번호 6개를 골라 winner 리스트에 담자!

    winner=[]
    for i in range(1,6):
        winner.append(res[f'drwtNo{i}'])
    print(winner)

    picked= random.sample(range(1,46), 6)

    matched = len(set(winner) & set(picked))

    if matched ==6:
        result= '1등입니다, 퇴사'
    elif matched ==5:
        result = '3등입니다. 퇴사는 위험, 휴가 ㄱㄱ'
    elif matched == 4:
        result ="4등입니다. 휴가 ㄱㄱ"
    elif matched == 3:
        result = '5등입니다. 다시 로또 구입 ㄱㄱ'
    else:
        result = '꽝 다음기회에'



    context={
        'result':result,
        'winner': winner,
        'name': name,
    }

    return render(request, 'pages/jackpot.html', context)


def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name= request.POST.get('name')
    password= request.POST.get('password')
    context={
        'name':name,
        'password':password
    }
    return render(request,'pages/user_create.html', context)

def static_example(request):
    return render(request, 'pages/static_example.html')