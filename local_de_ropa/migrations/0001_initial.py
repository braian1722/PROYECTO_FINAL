# Generated by Django 4.1.1 on 2022-10-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buzos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('talle', models.CharField(max_length=5)),
                ('color', models.CharField(max_length=40)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Camperas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('talle', models.CharField(max_length=5)),
                ('color', models.CharField(max_length=40)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jeans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('talle', models.CharField(max_length=5)),
                ('color', models.CharField(max_length=40)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Remeras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=40)),
                ('marca', models.CharField(max_length=40)),
                ('talle', models.CharField(max_length=5)),
                ('color', models.CharField(max_length=40)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
