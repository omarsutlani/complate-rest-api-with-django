# Generated by Django 4.2.4 on 2023-09-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
