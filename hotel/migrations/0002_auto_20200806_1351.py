# Generated by Django 3.1 on 2020-08-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelroom',
            name='image',
            field=models.ImageField(blank=True, upload_to='room-photo'),
        ),
    ]
