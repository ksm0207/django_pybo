from django import forms
from pybo.models import Question


# 아래 같은 클래스를 장고 form 이라고 부름 현재 ModelForm을 상속받음
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "content"]

