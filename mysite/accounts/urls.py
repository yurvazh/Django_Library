from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('users/', views.UsersView.as_view(), name="users_list")
]