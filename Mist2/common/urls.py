from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('like/<int:game_id>/', views.like_functionality, name='like_game'),
    path('comment/<int:game_id>/', views.add_comment, name='comment_game')
]
