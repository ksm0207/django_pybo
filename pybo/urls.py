from django.urls import path
from . import views

app_name = "pybo"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("answer/create/<int:get_question>", views.answer_create, name="answer_create"),
]
# get_question
