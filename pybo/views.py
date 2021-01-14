from django.shortcuts import render
from django.http import HttpResponse

# - index 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.
# - request는 사용자가 전달한 데이터를 확인할 때 사용된다.


def index(request):
    return HttpResponse("Hello World")

