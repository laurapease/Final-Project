# Generated by Django 3.1.3 on 2020-12-03 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20201203_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livestream',
            name='artist_img',
        ),
        migrations.AddField(
            model_name='livestream',
            name='photo_url',
            field=models.TextField(blank=True),
        ),
    ]