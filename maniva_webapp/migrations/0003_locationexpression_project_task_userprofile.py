# Generated by Django 3.1.2 on 2020-10-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maniva_webapp', '0002_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationExpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('client_name', models.CharField(max_length=1000, verbose_name='Client name')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('time_elapsed', models.IntegerField(blank=True, default=None, null=True, verbose_name='Elapsed time')),
                ('importance', models.IntegerField(verbose_name='Importance')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('login', models.CharField(max_length=25, verbose_name='Login')),
                ('password', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Phone number')),
                ('last_connection', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Date of last connection')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date of Birthday')),
            ],
        ),
    ]
