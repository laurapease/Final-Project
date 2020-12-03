# Generated by Django 3.1.3 on 2020-12-03 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_post_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('recources_link', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='livestream',
            name='description',
            field=models.TextField(),
        ),
    ]
