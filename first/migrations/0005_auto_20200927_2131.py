# Generated by Django 3.1.1 on 2020-09-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authordetail',
            name='tel',
            field=models.CharField(max_length=32),
        ),
    ]