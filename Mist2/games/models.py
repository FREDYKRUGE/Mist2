from enum import Enum

from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from django.db import models

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
    genre = models.CharField(choices=Genre.choices(), null=True, blank=True)
    release_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
