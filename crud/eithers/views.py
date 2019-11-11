from django.shortcuts import render
from .models import Question, Answer
from django.db.models import Count, Q

# Create your views here.
def detail(request, question_pk):
    question=Question.objects.annotation(
    sum_ab=Count(),
    count_a=Count('answer', filter=Q(answer_pick=0)),
    count_b=Count('answer', filter=Q(answer_pick=1)),
    ).get(pk=question_pk)



    question = Question.objects.prefetch_related('answer_set')
    answer=Answer.objects.selected_related('')