# Generated by Django 3.1 on 2021-04-11 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saleh', '0018_auto_20210411_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='salehw',
        ),
        migrations.RemoveField(
            model_name='book',
            name='your_stoory',
        ),
    ]