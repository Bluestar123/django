# Generated by Django 3.1.1 on 2020-09-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default='2020-09-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
