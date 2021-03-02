# Generated by Django 3.0.5 on 2021-03-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20210302_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='has_teacher_answered',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='test',
        ),
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(default=None, max_length=1024),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_content',
            field=models.TextField(default=None, max_length=1024, verbose_name='Zadaj pytanie'),
        ),
    ]