# Generated by Django 2.0.4 on 2018-04-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180410_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_sign',
            field=models.IntegerField(default=1234),
        ),
    ]
