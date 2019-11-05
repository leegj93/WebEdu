from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title= models.CharField(max_length=50)
    title_en= models.CharField(max_length=100)
    audience= models.IntegerField()
    open_date =models.DateTimeField()
    genre = models.CharField(max_length=50)
    watch_grade = models.CharField(max_length=50)
    score = models.FloatField()
    poster_url = models.TextField()
    description= models.TextField()

    def get_absolute_url(self):
            # ex) '/articles/10/'
        return reverse('movies:detail', args=[str(self.pk)])