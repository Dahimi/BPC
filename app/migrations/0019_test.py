# Generated by Django 4.0.5 on 2022-08-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_rename_game_advancement_game_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Game_Name', models.CharField(max_length=30)),
                ('Number', models.IntegerField()),
                ('Input', models.CharField(max_length=200)),
                ('Score', models.IntegerField()),
            ],
        ),
    ]
