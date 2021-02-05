from django.urls import path
from django.contrib.auth import views
from . import views as def_views

app_name = "common"

urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(template_name="common/login.html"),
        name="login",
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("signup/", def_views.signup, name="signup"),
]
