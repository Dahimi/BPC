# Generated by Django 4.0.5 on 2022-06-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_participant_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='Password',
            field=models.CharField(default='hello', max_length=30),
        ),
    ]
