# Generated by Django 2.2.5 on 2022-06-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20220624_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='houserule',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
