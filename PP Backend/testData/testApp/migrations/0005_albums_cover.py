# Generated by Django 4.2.6 on 2023-10-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0004_albums_date_albums_length_songs_date_songs_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='cover',
            field=models.ImageField(default='default.jpg', upload_to='cover_pic'),
        ),
    ]
