# Generated by Django 3.1.3 on 2020-12-03 02:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_livestream'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
