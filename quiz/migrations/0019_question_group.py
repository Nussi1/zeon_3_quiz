# Generated by Django 4.0.6 on 2022-07-25 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('quiz', '0018_customuser_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group'),
        ),
    ]
