# Generated by Django 2.2 on 2019-05-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20190513_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_status',
            field=models.CharField(choices=[('Available', 'Available'), ('Occupied', 'Occupied'), ('Out of Service', 'Out of Service')], default='Available', max_length=20),
        ),
    ]
