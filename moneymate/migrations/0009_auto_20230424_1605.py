# Generated by Django 3.2.18 on 2023-04-24 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneymate', '0008_category_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
        migrations.RemoveField(
            model_name='origin',
            name='user',
        ),
    ]