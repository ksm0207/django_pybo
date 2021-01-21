from django.shortcuts import render, redirect, reverse
from .models import Question

# - index 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.
# - request는 사용자가 전달한 데이터를 확인할 때 사용된다.


def index(request):

    # 데이터의 작성한 날짜를 역순으로 조회 order_by()
    # order_by() : 조회한 데이터를 특정 속성으로 정렬함 -create_date는 - 기호가 앞에 있으면 작성일시의 역순을 의미함
    question_list = Question.objects.order_by("-create_date")
    # 역순으로 조회된 데이터 변수에 저장
    context = {"question_list": question_list}

    # render 함수는 context에 있는 Question 모델 데이터 question_list를 templates/index.html 파일에 적용하여 HTML 코드로 변환한다.
    return render(request, "templates/index.html", context)


def detail(request, pk):

    get_question = Question.objects.get(pk=pk)
    context = {"get_question": get_question}
    print("Result =================", context, pk)

    if pk:
        print("??????", pk)
        return render(request, "templates/detail.html", context)
    else:
        print("Home")
        return redirect(reverse(""))
