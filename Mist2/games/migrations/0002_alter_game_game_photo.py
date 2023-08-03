# Generated by Django 4.1.5 on 2023-08-03 14:27

import Mist2.games.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images//', validators=[Mist2.games.validators.image_size_validator_5mb]),
        ),
    ]
