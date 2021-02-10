from django.contrib import admin
from .models import Question, Answer, Comment


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ["subject"]  # Admin 페이지에서 데이터 검색 기능 추가


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    pass


class CommnetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Answer)
admin.site.register(Comment)
