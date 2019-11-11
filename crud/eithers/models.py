from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length= 50)
    issue_a = models.CharField(max_length=50)
    issue_b = models.CharField(max_length=50)
    image_a= models.ImageField(blank=True, upload_to ='eithers/%Y/%m/%d')

class Answer(models.Model):
    question_id = models.IntegerField()
    pick =models.IntegerField()
    comment = models.TextField()