# Generated by Django 4.0.6 on 2022-07-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0020_question_qwty_participants_question_qwty_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='technique',
            field=models.IntegerField(choices=[(0, 'Multiple Choices')], default=4, verbose_name='Type of Question'),
        ),
    ]
