# Generated by Django 4.2.6 on 2023-10-29 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0009_reviews_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='like',
            field=models.IntegerField(default='0'),
        ),
    ]
