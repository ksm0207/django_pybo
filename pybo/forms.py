from django import forms
from pybo.models import Question
from pybo.models import Answer


# 아래 같은 클래스를 장고 form 이라고 부름 현재 ModelForm을 상속받음
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "content"]
        labels = {"subject": "제목", "content": "내용"}


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]
        labels = {"content": "답변내용"}

