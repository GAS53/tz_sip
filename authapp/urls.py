from django.urls import path, include
from authapp.views import CreaterUserAPI, LoginViewAPI, RefreshTokenAPI

app_name = 'authapp'

urlpatterns = [
    path("register/", CreaterUserAPI.as_view()),
    path("login/", LoginViewAPI.as_view()),
    path("refresh/", RefreshTokenAPI.as_view()),

]