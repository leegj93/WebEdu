from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.

class Article(models.Model):
    title= models.CharField(max_length= 50)
    content= models.CharField(max_length= 100)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    # image= models.ImageField(blank=True ,upload_to='article/%Y/%m/%d')
    image=ProcessedImageField(
        processors=[Thumbnail(200, 300)],
        format= 'JPEG', #저장 포멧
        options={'quality': 90}, # 추가 옵션
        upload_to='article/images' # 저장 위치 MEDIA_ROOT/articles/images
    )