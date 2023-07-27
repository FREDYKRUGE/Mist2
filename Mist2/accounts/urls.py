from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import LoginUserView, LogoutUserView, RegisterUserView, UserEditView, ProfileDetailView, ProfileDeleteView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-details'),
    path('profile/<int:pk>/edit/', UserEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]
