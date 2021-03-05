# Generated by Django 3.0.5 on 2021-03-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_account_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='group',
        ),
        migrations.AddField(
            model_name='account',
            name='group_id',
            field=models.IntegerField(default=0, verbose_name='Grupa'),
        ),
    ]
