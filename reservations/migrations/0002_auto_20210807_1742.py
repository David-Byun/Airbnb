# Generated by Django 2.2.5 on 2021-08-07 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookedday',
            options={},
        ),
        migrations.AlterField(
            model_name='bookedday',
            name='created',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='bookedday',
            name='updated',
            field=models.DateTimeField(default=''),
        ),
    ]
