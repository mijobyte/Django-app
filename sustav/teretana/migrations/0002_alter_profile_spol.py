# Generated by Django 4.2.7 on 2024-03-07 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teretana', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='spol',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
