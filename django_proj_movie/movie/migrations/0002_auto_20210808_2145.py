# Generated by Django 3.2.6 on 2021-08-08 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='movie_name',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='movie_name',
            new_name='movie',
        ),
    ]
