# Generated by Django 4.0.5 on 2022-08-09 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='Number',
            new_name='Game_Id',
        ),
        migrations.RemoveField(
            model_name='test',
            name='Game_Name',
        ),
        migrations.AddField(
            model_name='test',
            name='Test_Id',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]
