# Generated by Django 2.2.7 on 2019-11-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='articles/%Y/%m/%d'),
        ),
    ]
