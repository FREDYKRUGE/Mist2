# urls.py
from django.urls import path
from . import views
from .views import GameCreateView, GameEditView, GameDeleteView, GameDetailsView

urlpatterns = [
    path('game/create/', GameCreateView.as_view(), name='create_game'),
    path('game/<int:pk>/', GameDetailsView.as_view(), name='details_game'),
    path('game/<int:pk>/edit/', GameEditView.as_view(), name='edit_game'),
    path('game/<int:pk>/delete/', GameDeleteView.as_view(), name='delete_game'),
    path('game/<int:pk>/details/', GameDetailsView.as_view(), name='details_game'),
]
