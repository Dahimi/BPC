# Generated by Django 4.0.5 on 2022-08-08 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_advancement_game_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='Tests',
        ),
    ]