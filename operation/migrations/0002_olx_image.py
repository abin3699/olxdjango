# Generated by Django 4.2.5 on 2023-09-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='olx',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
