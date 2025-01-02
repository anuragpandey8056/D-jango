# Generated by Django 5.1.4 on 2024-12-31 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadharNo', models.IntegerField(unique=True)),
                ('CreatedDate', models.DateTimeField()),
                ('createdBY', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=254)),
                ('dob', models.DateTimeField()),
                ('adharno', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='myapp.adhar', to_field='aadharNo')),
            ],
        ),
    ]
