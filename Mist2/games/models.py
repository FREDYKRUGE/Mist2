from enum import Enum

from django.core.validators import MinLengthValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from django.db import models
from .validators import image_size_validator_5mb
from django import forms

UserModel = get_user_model()


class Genre(Enum):
    ACTION = 'Action'
    PUZZLE = 'Puzzle'
    HORROR = 'Horror'
    STRATEGY = 'Strategy'
    PLATFORMER = 'Platformer'

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class Game(models.Model):
    name = models.CharField(max_length=30, validators=[MinLengthValidator(2)],
                            null=False, blank=False)
    genre = models.CharField(max_length=10, choices=Genre.choices(), null=True, blank=True)
    release_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)
    game_photo = models.ImageField(blank=True, null=True, validators=(image_size_validator_5mb,),
                                   upload_to='images//')
    size = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    description = models.TextField(max_length=300, validators=(MinLengthValidator(10),), blank=True, null=True)

    def __str__(self):
        return self.name


class GameEditForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'genre', 'game_photo', 'size', 'price', 'description')
        exclude = ('release_date', 'user')
        labels = {
            'name': 'Name of the game',
            'genre': 'Genre',
            'game_photo': 'Game photo',
            'size': 'Size',
            'price': 'Price',
            'description': 'Description'
        }

