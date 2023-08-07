from django.contrib import admin

from Mist2.common.models import *


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time_of_publication', 'to_game')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
