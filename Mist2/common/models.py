from django.contrib.auth import get_user_model
from django.db import models

from Mist2.games.models import Game

UserModel = get_user_model()


class Comment(models.Model):
    comment_text = models.TextField(max_length=300, blank=False, null=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    to_game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='likes')


class Meta:
    ordering = ['-date_time_of_publication']
