# Generated by Django 3.0.6 on 2021-01-20 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='photo',
            field=models.ImageField(upload_to='photo'),
        ),
    ]