# Generated by Django 3.0.5 on 2021-03-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentOutput',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_task_id', models.IntegerField()),
                ('snumber', models.CharField(max_length=6)),
                ('output_file', models.FileField(upload_to='task/promela/output')),
                ('points', models.IntegerField(default=0)),
                ('has_been_graded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentTask',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('task_id', models.IntegerField()),
                ('task_file', models.FileField(upload_to='task/promela/student_files')),
                ('snumber', models.CharField(max_length=6)),
                ('group_id', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('group_id', 'task_id'),
            },
        ),
        migrations.CreateModel(
            name='TeacherTask',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('task_name', models.TextField(max_length=100)),
                ('max_points', models.FloatField(default=0)),
                ('file', models.FileField(upload_to='task/promela/teacher_ltl')),
                ('group_id', models.IntegerField(default=0)),
            ],
        ),
    ]