# Generated by Django 2.2 on 2019-05-13 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20190513_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_status',
            field=models.CharField(choices=[('Available', 'Available'), ('Occupied', 'Occupied'), ('Out of Service', 'Out of Service')], max_length=20, null=True),
        ),
    ]
