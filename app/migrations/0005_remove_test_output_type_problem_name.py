# Generated by Django 4.0.5 on 2022-06-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_problem_test_remove_participant_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='Output_type',
        ),
        migrations.AddField(
            model_name='problem',
            name='name',
            field=models.CharField(default='la somme de deux nombres', max_length=200),
            preserve_default=False,
        ),
    ]
