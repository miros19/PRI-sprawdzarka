# Generated by Django 3.1.4 on 2021-01-09 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='groups',
            fields=[
                ('nazwa', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('przedmiot', models.CharField(max_length=32)),
                ('opis', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Plagiaty',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('snumber', models.IntegerField(max_length=6)),
                ('sprawko_name', models.CharField(max_length=32)),
                ('plagiat_percentage', models.IntegerField(max_length=3)),
                ('with_who', models.IntegerField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Szablon_zadan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('przedmiot', models.CharField(max_length=32)),
                ('temat', models.CharField(max_length=32)),
                ('nr_zadania', models.IntegerField(max_length=2)),
                ('pkt_zadanie', models.IntegerField(max_length=2)),
                ('tresc', models.CharField(max_length=2000)),
                ('pop_roz', models.CharField(max_length=2000)),
            ],
        ),
    ]