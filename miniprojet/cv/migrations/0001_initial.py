# Generated by Django 4.1.2 on 2022-11-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competance_languistique', models.CharField(max_length=80)),
                ('competance_technique', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=80)),
                ('date', models.DateField()),
                ('lieu', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=80)),
                ('date', models.DateField()),
                ('lieu', models.CharField(max_length=80)),
            ],
        ),
    ]