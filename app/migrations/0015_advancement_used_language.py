# Generated by Django 4.0.5 on 2022-08-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_advancement_game_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancement',
            name='Used_Language',
            field=models.CharField(default='Python', max_length=30),
            preserve_default=False,
        ),
    ]