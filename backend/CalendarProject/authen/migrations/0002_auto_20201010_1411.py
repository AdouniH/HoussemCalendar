# Generated by Django 3.1.2 on 2020-10-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='code',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
