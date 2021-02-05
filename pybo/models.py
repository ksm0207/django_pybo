from django.db import models
from django.contrib.auth.models import User


# 질문 모델 생성
class Question(models.Model):
    # 제목 / 내용 / 작성일시 / 이미지 Model 생성
    subject = models.CharField(max_length=200)  # 최대 200자 까지 입력 가능
    content = models.TextField()
    create_date = models.DateTimeField()
    photo = models.ImageField(upload_to="photo")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
    )  # 계정이 삭제되면 연결된 질문 데이터 삭제

    def __str__(self):
        return self.subject


# 답변 모델 생성
class Answer(models.Model):
    # 질문에 대한 답변을 하기 위해선 Question 모델을 속성을 가진다
    # A Model 이 B Model의 속성을 가진다면 ForeignKey를 사용한다 A -- B 와 연결 한다는것
    # on_delete 는 답변에 연결된 질문이 삭제되면 답변도 삭제하도록 설정한다
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
    )  # 계정이 삭제되면 연결된 질문 데이터 삭제

    def __str__(self):
        return self.content

