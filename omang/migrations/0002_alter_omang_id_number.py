# Generated by Django 4.2 on 2023-09-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omang', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='omang',
            name='ID_Number',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]