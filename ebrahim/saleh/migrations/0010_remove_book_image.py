# Generated by Django 3.1 on 2021-04-10 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saleh', '0009_auto_20210410_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
    ]