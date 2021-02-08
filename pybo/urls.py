from django.urls import path
from . import views

app_name = "pybo"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("answer/create/<int:get_question>", views.answer_create, name="answer_create"),
    path("question/create/", views.question_create, name="question_create"),
    path(
        "question/modify/<int:get_question>/",
        views.question_modify,
        name="question_modify",
    ),
    path(
        "question/delete/<int:get_question>/",
        views.question_delete,
        name="question_delete",
    ),
    path("answer/modify<int:answer_id>/", views.answer_modify, name="answer_modify"),
    path("answer/delete<int:answer_id>/", views.answer_delete, name="answer_delete"),
]
