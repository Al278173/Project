# Generated by Django 2.2 on 2019-05-04 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190503_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='attend',
        ),
    ]
