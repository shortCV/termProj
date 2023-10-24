# Generated by Django 4.2.6 on 2023-10-19 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_remove_task_out'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.ManyToManyField(to='testApp.artists')),
            ],
        ),
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.ManyToManyField(to='testApp.artists')),
                ('song', models.ManyToManyField(to='testApp.songs')),
            ],
        ),
    ]