# Generated by Django 4.0.6 on 2022-07-25 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('quiz', '0017_alter_participantanswer_participant_ball_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group'),
        ),
    ]
