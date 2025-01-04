from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="index"),
    path("home/", home, name="home"),
    path("contact/", contact, name="contact"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("profile/", profile, name="profile"),
    path("generate_image/", generate_image, name="generate_image"),
    path('delete_account/', delete_account, name='delete_account'),
]
