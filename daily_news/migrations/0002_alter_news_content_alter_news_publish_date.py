# Generated by Django 4.0.4 on 2022-04-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='publish_date',
            field=models.DateTimeField(default=''),
        ),
    ]
