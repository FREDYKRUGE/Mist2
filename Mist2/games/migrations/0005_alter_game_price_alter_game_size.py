# Generated by Django 4.1.5 on 2023-07-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='size',
            field=models.PositiveIntegerField(),
        ),
    ]
