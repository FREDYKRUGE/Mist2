# Generated by Django 4.1.5 on 2023-08-07 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_alter_game_price_alter_game_size'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='to_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='games.game'),
        ),
    ]
