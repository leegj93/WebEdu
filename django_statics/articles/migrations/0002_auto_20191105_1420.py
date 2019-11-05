# Generated by Django 2.2.6 on 2019-11-05 05:20

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='article/images'),
        ),
    ]
