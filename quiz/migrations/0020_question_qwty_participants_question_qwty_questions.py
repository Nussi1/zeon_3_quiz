# Generated by Django 4.0.6 on 2022-07-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0019_question_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='qwty_participants',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='qwty_questions',
            field=models.IntegerField(default=0),
        ),
    ]
