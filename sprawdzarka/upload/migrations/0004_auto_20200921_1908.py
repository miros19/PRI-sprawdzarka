# Generated by Django 3.1.1 on 2020-09-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20200921_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='task',
            field=models.FileField(upload_to='task/tasklist/'),
        ),
    ]
