# Generated by Django 3.1.3 on 2020-12-03 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_auto_20201203_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livestream',
            name='artist_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
