from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Question, Answer
from django.contrib import messages
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# from tkinter import *

# - index 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.
# - request는 사용자가 전달한 데이터를 확인할 때 사용된다.


def index(request):

    # 데이터의 작성한 날짜를 역순으로 조회 order_by()
    # order_by() : 조회한 데이터를 특정 속성으로 정렬함 -create_date는 - 기호가 앞에 있으면 작성일시의 역순을 의미함
    question_list = Question.objects.order_by("-create_date")
    # 역순으로 조회된 데이터 변수에 저장

    #  페이지 기능 추가 02-01
    page = request.GET.get("page", "1")  # 페이지 GET 방식 요청

    paginator = Paginator(question_list, 10)  # 페이지 게시물 10개씩 보여주기
    page_obj = paginator.get_page(page)
    print(page_obj)

    context = {"question_list": page_obj}

    # render 함수는 context에 있는 Question 모델 데이터 question_list를 templates/index.html 파일에 적용하여 HTML 코드로 변환한다.
    return render(request, "templates/index.html", context)


def detail(request, pk):
    # Question.get() --> 404() 으로 변경
    # get_object_or_404 함수는 모델의 기본키를 이용하여 모델 객체 한 건을 반환한다. pk에 해당하는 건이 없으면 오류 대신 404 페이지를 반환한다.
    # 01-22 get_object_or_404 --> get() 함수 변경

    try:
        get_question = Question.objects.get(pk=pk)
        context = {"get_question": get_question}
        # 존재 하지않는 페이지 입력했을때 예외처리 완료
    except Question.DoesNotExist:
        # return render(request, "templates/index.html")
        messages.error(request, "조회된 질문이 없습니다.")
        return redirect("pybo:index")

    return render(request, "templates/detail.html", context)


# 답변 등록 기능 함수
@login_required(login_url="common:login")
def answer_create(request, get_question):
    question = Question.objects.get(pk=get_question)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 필드 적용
            print("Answer User ==== ", answer.author)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            # redirect 함수의 첫 번째 인수에는 이동할 페이지의 별칭을, 두 번째 인수에는 해당 URL에 전달해야 하는 값을 입력한다.
            return redirect("pybo:detail", pk=get_question)
    else:
        form = AnswerForm()
    context = {"get_question": get_question, "form": form}
    print("Context !! ", context)
    return render(request, "templates/detail.html", context)

    # answer = Answer(
    # question=question,
    # content=request.POST.get("content"),
    # create_date=timezone.now(),

    # print("Request ====", request)
    # print("Answer ==== ", answer)
    # print("ID === ", get_question)
    # answer_create 함수의 get_question 매개변수에는 URL 매핑 정보값이 넘어온다.
    # 예를 들어 /pybo/answer/create/2가 요청되면 get_question 에는 2가 넘어온다.
    # request 매개변수에는 pybo/question_detail.html에서 textarea에 입력된 데이터가 담겨 넘어온다.
    # 이 값을 추출하기 위한 코드가 바로 request.POST.get('content')이다.


# 질문 등록 기능 함수
@login_required(login_url="common:login")
def question_create(request):
    print("Request ===", request)

    if request.method == "POST":  # 조건이 True일때
        # 화면에서 전달받은 데이터로 폼의 값이 채워지는 객체 생성이 됨
        form = QuestionForm(request.POST)
        # 위 조건이 True 일때 form이 유효한지 검사진행
        if form.is_valid():  # POST 요청으로 받은 form이 유효한가?
            question = form.save(commit=False)  # Model 데이터를 임시 저장 Read.md 참고
            question.author = request.user
            print("Question User ===== ", question.author)
            question.create_date = timezone.now()
            question.save()
            return redirect("pybo:index")
    else:
        # QuestionForm 클래스로 생성한 객체 form을 사용
        # 질문 등록하기 위한 사용하는 장고 form
        # 입력값이 없는 객체 생성
        form = QuestionForm()

    context = {"form": form}
    return render(request, "templates/question_form.html", context)


# 게시물 수정 기능 함수 추가
def question_modify(request, get_question):

    question = Question.objects.get(pk=get_question)

    # 로그인한 사용자 와 수정하려는 글쓴이와 다르면 오류메시지 출력
    if request.user != question.author:
        messages.error(request, "올바르지 않은 요청입니다.")
        return redirect("pybo:detail", pk=get_question)

    if request.method == "POST":
        # 질문 수정을 위해 값 덮어쓰기
        form = QuestionForm(request.POST, instance=question)
        print("form ============ ", form)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect("pybo:detail", pk=get_question)
    else:
        # GET 요청으로 질문 수정 화면이 나타남
        # [질문 수정 화면에 기존 제목, 내용 반영]
        form = QuestionForm(instance=question)
    context = {"form": form}

    return render(request, "templates/question_form.html", context)


# 질문 삭제 함수 추가
def question_delete(request, get_question):

    question = Question.objects.get(pk=get_question)

    if request.user != question.author:
        messages.error(request, "삭제권한이 없습니다")
        return redirect("pybo:detail", pk=get_question)

    question.delete()
    return redirect("pybo:index")


# 답변 수정 함수 추가
def answer_modify(request, answer_id):

    answer = Answer.objects.get(pk=answer_id)

    if request.user != answer.author:
        messages.error(request, "유효하지 않은 요청입니다.")

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect("pybo:detail", pk=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {"form": form}

    return render(request, "templates/answer_form.html", context)


# 답변 삭제 함수 추가
def answer_delete(request, answer_id):

    answer = Answer.objects.get(pk=answer_id)
    if request.user != answer.author:
        messages.error(request, "유효하지 않은 요청입니다.")
        return redirect("pybo:detail", pk=answer.question.id)

    answer.delete()
    return redirect("pybo:detail", pk=answer.question.id)
