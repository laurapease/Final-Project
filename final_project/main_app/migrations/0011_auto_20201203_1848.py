# Generated by Django 3.1.3 on 2020-12-03 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20201203_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='recource_link',
            new_name='resource_link',
        ),
    ]