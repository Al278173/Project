# Generated by Django 2.2 on 2019-05-04 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20190504_0608'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('first_name', 'last_name')},
        ),
        migrations.RemoveField(
            model_name='student',
            name='registered',
        ),
    ]
