# django_pybo
# Python Web 프로그래밍 학습시작
# 게시판 만들기 
# 출처 https://wikidocs.net/book/4223



##### 2021-01-14 
#### Model 만들기
#### 질문 목록 및 질문 상세 기능 구현하기

#### Filter VS GET 

#### ※ 조건으로 Question 모델 데이터 조회하기
#### 이전 단계에서는 Question 모델 데이터를 모두 조회했다. 조건을 주어 Question 모델 데이터를 조회하고 싶다면 filter 함수를 사용하면 된다.

##### [명령 프롬프트]
##### >>> Question.objects.filter(id=1) "class django.db.models.query.QuerySet"
##### <QuerySet [<Question: pybo가 무엇인가요?>]>
##### filter 함수는 조건에 해당하는 데이터를 모두 찾아준다. 지금은 유일한 값인 id를 조건에 사용했으므로 Question 모델 데이터 하나만 나왔다.
##### 하지만 filter 함수는 1개 이상의 데이터를 반환한다. 다만 filter 함수는
##### 반환값이 리스트 형태인 QuerySet이므로 정말로 1개의 데이터만 조회하고 싶다면 filter 함수 대신 get 함수를 쓰는 것이 좋다.

#### ※ Question 모델 데이터 하나만 조회하기
#### get 함수를 사용하면 리스트가 아닌 데이터 하나만 조회할 수 있다.

##### [명령 프롬프트]
##### >>> Question.objects.get(id=1) "class pybo.models.Question"
##### <Question: pybo가 무엇인가요?>
##### 반환값을 보면 QuerySet이 아니라 Question이다. 여기서 filter 함수와 get 함수의 차이점을 알 수 있다.
##### filter 함수는 여러 건의 데이터를 반환하지만, get 함수는 단 한 건의 데이터를 반환한다. 두 함수의 차이점을 꼭  알아 두기 바란다.

#### ※ 제목의 일부를 이용하여 데이터 조회하기
#### subject에 "장고"라는 문자열이 포함된 데이터를 조회하려면 조건에 subject__contains를 이용하면 된다.
#### 이때 subject와 contains 사이의 언더스코어는 1개가 아니라 2개이다. 장고 셸에서 다음 코드를 입력해 보자.

##### [명령 프롬프트]
##### >>> Question.objects.filter(subject__contains='장고')
##### <QuerySet [<Question: 장고 모델 질문입니다.>]>
##### subject__contains='장고'의 의미는 'subject 속성에 '장고'라는 문자열이 포함되어 있는가?'이다.
##### 이 밖에도 filter 함수의 사용 방법은 무궁무진하다. 자세한 filter 함수의 사용 방법은 장고 공식 문서를 참조하자.

##### - 장고는 외워서 사용할 수 있는 프레임워크가 아니므로 장고 공식 문서를 자주 참고하는 습관을 들이는 것이 좋다.
##### - 장고 공식 문서(데이터 조회 관련): docs.djangoproject.com/en/3.0/topics/db/queries

###### ※ 연결된 데이터 알아보기
###### https://wikidocs.net/70650

###### ================================================================================================================

##### 2021-01-21
##### 장고는 앱 하위에 있는 templates 디렉터리를 자동으로 템플릿 디렉터리로 인식한다

#### 장고는 DIRS에 설정한 디렉터리 외에도 특정 앱(예를 들어 pybo 앱) 디렉터리 하위에 있는 templates라는 이름의 디렉터리를 자동으로 템플릿 디렉터리로 인식한다. 예를 들어 다음과 같은 pybo 앱 디렉터리 밑의 templates #### 디렉터리는 별다른 설정을 하지 않아도 템플릿 디렉터리로 인식된다.

#### C:\projects\mysite\pybo\templates
#### 하지만 필자는 이 방법을 권장하지 않는다. 왜냐하면 하나의 사이트에서 여러 앱을 사용할 때 여러 앱의 화면을 구성하는 템플릿은 한 디렉터리에 모아 관리하는 편이 여러모로 좋기 때문이다. 예를 들어 여러 앱이 
#### 공통으로  사용하는 공통 템플릿을 어디에 저장해야 할지 생각해 보면 왜 이런 방법을 선호하는지 쉽게 이해될 것이다.
#### 그래서 파이보는 템플릿 디렉터리를 mysite/pybo/templates와 같은 방식이 아니라 mysite/templates/pybo 같은 방식으로 관리하며, 공통으로 사용하는 템플릿은 C:/projects/mysite/templates에 저장한다.
##### 구분	경로
##### 공통 템플릿 디렉터리	C:/projects/mysite/templates
##### pybo 앱 템플릿 디렉터리	C:/projects/mysite/templates/pybo


##### 템플릿 태그 의미
##### {% if question_list %} question_list가 있다면
##### {% for question in question_list %}	question_list를 반복하며 순차적으로 question에 대입
##### {{ question.id }}	for 문에 의해 대입된 question 객체의 id 출력
##### {{ question.subject }}	for 문에 의해 대입된 question 객체의 subject 출력
##### - 템플릿 태그에서 사용된 question_list가 바로 render 함수에서 템플릿으로 전달한 Question 모델 데이터이다.
##### - 만약 템플릿 태그의 자세한 내용이 궁금하다면 장고 공식 문서를 참고하자.
##### - 템플릿 장고 공식 문서 주소: docs.djangoproject.com/en/3.0/topics/templates

#### 템플릿 태그! 3가지 유형만 정리하면 끝!

#### 장고의 템플릿 태그는 분기, 반복, 객체 출력이라는 3가지 유형만 알면 된다. 분기 템플릿 태그는 다음과 같다.
#### 문법을 보면 알겠지만 파이썬의 if 문과 다르지 않다. 다만 if 문이 끝나는 부분에 {% endif %}를 사용하는 점만 다르다.

#### {% if 조건문1 %}
####     <p>조건문1에 해당되는 경우</p>
#### {% elif 조건문2 %}
####     <p>조건문2에 해당되는 경우</p>
#### {% else %}
####     <p>조건문1, 2에 모두 해당되지 않는 경우</p>
#### {% endif %}
#### 반복 템플릿 태그는 다음과 같다. 이 역시 파이썬의 for 문과 다르지 않으며, 역시 for 문의 마지막은 {% endfor %}로 닫아야 한다.

#### {% for item in list %}
####     <p>순서: {{ forloop.counter }} </p>
####     <p>{{ item }}</p>
#### {% endfor %}
#### 또한 반복 템플릿 안에서는 forloop 객체를 사용할 수도 있다. forloop 객체는 반복 중 유용한 값을 제공한다.

#### ※ forloop 객체 속성 설명
#### forloop.counter	for 문의 순서로 1부터 표시
#### forloop.counter0	for 문의 순서로 0부터 표시
#### forloop.first	for 문의 첫 번째 순서인 경우 True
#### forloop.last	for 문의 마지막 순서인 경우 True
#### 객체 출력 템플릿 태그는 다음과 같다. 객체에 속성이 있으면 파이썬과 동일한 방법으로 점(.) 연산자를 사용한다.

#### {{ question }}
#### {{ question.id }}
#### {{ question.subject }}

###### =================================================================================

##### 2021-01-21
##### 2-05 URL 더 똑똑하게 사용하기

#### /pybo/{{ question.id }}는 질문 상세를 위한 URL 규칙이다.
#### 하지만 이런 URL 규칙은 프로그램을 수정하면서 /pybo/question/2/ 또는 /pybo/2/question/으로 수정될 가능성도 있다.
#### 이런 식으로 URL 규칙이 자주 변경된다면 템플릿에 사용된 모든 href값들을 일일이 찾아 수정해야 한다. URL 하드 코딩의 한계인 셈이다.
#### 이런 문제를 해결하려면 해당 URL에 대한 실제 주소가 아닌 주소가 매핑된 URL 별칭을 사용해야 한다.

##### [1] pybo/urls.py 수정하여 URL 별칭 사용하기
#### 템플릿의 href에 실제 주소가 아니라 URL 별칭을 사용하려면 우선 pybo/urls.py 파일을 수정해야 한다.
#### path 함수에 있는 URL 매핑에 name 속성을 부여하자.
#### path('<int:question_id>/', views.detail, name='detail'), detail 이라는 URL 별칭이 생김
#### path('', views.index, name='index'), index 라는 URL 별칭 만들기

##### [2] pybo/question_list.html 템플릿에서 URL 별칭 사용하기
#### 1단계에서 만든 별칭을 템플릿에서 사용하기 위해 /pybo/{{ question.id }}를 {% url 'detail' question.id %}로 변경하자.
#### question.id는 URL 매핑에 정의된 <int: question_id>를 의미한다.

##### URL 네임스페이스 알아보기
#### 여기서 한 가지 더 생각할 문제가 있다. 현재의 프로젝트에서는 pybo 앱 하나만 사용하지만
#### 이후 pybo 앱 이외의 다른 앱이 프로젝트에 추가될 수도 있다. 이때 서로 다른 앱에서 같은 URL 별칭을 사용하면 중복 문제가 생긴다.
#### 이 문제를 해결하려면 pybo/urls.py 파일에 네임스페이스(namespace)라는 개념을 도입해야 한다. 네임스페이스는 쉽게 말해 각각의 앱이 관리하는 독립된 이름 공간을 말한다.
#### 사용방법은 urls.py 파일에 간단히 app_name 변수에 네임스페이스 이름을 저장하면 된다.

###### =================================================================================

##### 2021-01-25
#### 2-06 답변 등록 기능 만들기

#### {% csrf_token %}
#### 이 코드는 보안 관련 항목이다 
#### {% csrf_token %}는 form 엘리먼트를 통해 전송된 데이터(답변)가 실제로 웹 브라우저에서 작성된 데이터인지 판단하는 검사기 역할을한다. 
#### 해킹처럼 올바르지 않은 방법으로 데이터가 전송되면 서버에서 발행한 csrf_token값과 해커가 보낸 csrf_token값이 일치하지 않으므로
#### 오류를 발생시켜 보안을 유지할 수 있다.

#### csrf_token은 장고의 기본 기능이다
#### csrf_token을 사용하려면 장고에 CsrfViewMiddleware라는 미들웨어를 추가해야 한다.
#### 하지만 이 미들웨어는 장고 프로젝트 생성 시 자동으로 config/settings.py 파일의 MIDDLEWARE라는 항목에 추가되므로 여러분이 직접 #### 입력할 필요는 없다.
#### 
##### def answer_create(request, question_id):
    
##### question = get_object_or_404(Question, pk=question_id)
#### 이 값을 추출하기 위한 코드가 바로 request.POST.get('content')이다.
#### 그리고 Question 모델을 통해 Answer 모델 데이터를 생성하기 위해 question.answer_set.create를 사용했다.
#### - request.POST.get('content')는 POST 형식으로 전송된 form 데이터 항목 중 name이 content인 값을 의미한다.
#### - Answer 모델이 Question 모델을 Foreign Key로 참조하고 있으므로 question.answer_set 같은 표현을 사용할 수 있다.
#### question.answer_set.create(content=request.POST.get("content"), create_date=timezone.now())

###### =================================================================================


##### 2021-01-26
#### 2-07 화면 꾸미기

##### 웹 페이지에 스타일시트 적용하기
#### 웹 페이지에 디자인을 적용하려면 스타일시트(CSS)를 사용해야 하며, 스타일시트를 파이보에 적용하려면 CSS 파일이 스태틱(static)
#### 디렉터리에 있어야 한다.

#### CSS 파일은 장고에서 정적(static)파일로 분류한다. 정적 파일은 주로 이미지(.png, .jpg)나 자바스크립트(.js), 스타일시트(.css)
#### 같은 파일을 의미한다.

#### [1] 설정 파일에 스태틱 디렉터리 위치 추가하기
#### config/settings.py 파일을 열어 STATICFILES_DIRS에 스태틱 디렉터리 경로를 추가하자. BASE_DIR / 'static'은 C:/projects/
#### mysite/ static을 의미한다.

#### ※Django 프로젝트 홈 디렉토리 (settings.py에서의 BASE_DIR) 밑에 "static" 이라는 서브 폴더를 만들어 그곳에 static 파일들을 넣는다
#### static 폴더에 파일들을 넣고 사용하기 위해서는 settings.py 에 하나의 셋팅을 추가해 주어야 한다.
#### 즉, settings.py 파일에서 아래와 같이 static 파일들을 찾는 경로를 나타내는 STATICFILES_DIRS 라는 변수를 설정해야 한다.
#### 경로가 여러 개일 수 있지만, 여기서는 BASE_DIR/static 폴더 하나를 지정하였다.

#### 변수 = STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


#### [2] 스태틱 디렉터리 만들고 스타일시트 작성하기
#### 프로젝트 루트 디렉터리에 static이라는 이름의 디렉터리를 생성하자. 루트 디렉터리는 C:/ projects/mysite를 의미한다.

#### [3] 질문 상세 템플릿에 스타일 적용하기
#### 템플릿 상단에 {% load staticfiles %} 태그를 먼저 명시해 주어야 한다
#### pybo/question_detail.html 파일에 style.css 파일을 적용해 보자. 스태틱 파일을 사용하기위해 템플릿 파일 맨 위에 
#### {% load static %}  태그를 삽입하고, link 엘리먼트 href 속성에 {% static 'style.css' %}를 적자.

###### =================================================================================

##### 2021-01-26
##### 2-09 표준 HTML과 템플릿 상속 사용해 보기

#### 표준 HTML 구조는 어떻게 생겼을까?
#### 표준 HTML 문서의 구조는 다음과 같이 html, head, body 엘리먼트가 있어야 하며
#### CSS 파일은 head 엘리먼트 안에 있어야 한다. 또한 head 엘리먼트 안에는 meta, title 엘리먼트 등이 포함되어야 한다.

#### 템플릿을 표준 HTML 구조로 바꾸기
#### 장고는 템플릿 상속(extends) 기능을 제공한다. 여기서는 단순히 템플릿을 표준 HTML 구조로 바꾸는 것이 아니라 템플릿 상속 기능까지 사용할것이다

#### [1] 템플릿 파일의 기본 틀 작성하기
#### body 엘리먼트에 {% block content %}와 {% endblock %} 템플릿 태그가 있다. 바로 이 부분이 이후 base.html 템플릿 파일을 상속한 파일에서 구현해야 하는 영역이 된다. 

###### =================================================================================

##### 2021-01-27
##### 2-09 질문 등록 기능 만들기
#### [1] 장고 폼 작성하기
#### 장고 폼은 2개의 폼으로 구분할 수 있는데, forms.Form을 상속받으면 form 
#### forms.ModelForm을 상속받으면 Model Form이라 부른다. 여기서는 form.ModelForm을 상속받아 Model Form을 만들었다.
#### Model Form 은 말 그대로 모델과 연결된 폼이며, 모델 폼 객체를 저장하면 연결된 모델의 데이터를 저장할 수 있다
#### 장고 모델 폼은 내부 클래스로 Meta 클래스를 반드시 가져야 하며, Meta 클래스에는 모델 폼이 사용할 모델과 모델의 필드들을 적어야 한다.
#### Model Field는 사용하고자 하는 field를 적어주면 된다

#### [2] 입력 데이터 저장하기
#### QuestionForm 객체도 GET 방식과 POST 방식일 경우 다르게 생성한 것에 주목하자.
#### GET 방식의 경우 QuestionForm()과 같이 입력값 없이 객체를 생성했고 POST 방식의 경우에는 QuestionForm(request.POST)처럼
#### 화면에서 전달받은 데이터로 폼의 값이 채워지도록 객체를 생성했다.
#### form.is_valid 함수는 POST 요청으로 받은 form이 유효한지 검사한다. 폼이 유효하지 않다면 폼에 오류가 저장되어 화면에 전달될 것이다.

#### [3] commit=False
#### Question 모델 데이터를 저장하기 위해 commit=False를 사용하였는데 이것은
#### 데이터를 임시저장을 의미한다 실제 데이터는 아직 저장되지 않은 상태이며 사용하는 이유는 
#### Form으로 질문 데이터를 저장할 경우 create_date에 값이 설정되지 않아 오류가 발생하기 때문에 이런 방도를 세운것이다
#### 그래서 먼저 임시저장을 한 후 Question 객체를 반환받어 create_date 에 값을 설정을 해준것이다

###### =================================================================================

##### 2021-01-29

#### 3-01 내비게이션 기능 추가하기
#### ※ 현재 게시판 기능은 질문 등록 조회 답변 , 답변 등록 조회 기능 밖에 없고 편의 기능 또한 없다
#### 그중 메인 페이지로 돌아갈 수 있는 장치가 없으므로 이런 불편함을 해소하기 위해 내비게이션바를 만들어본다

#### [1] 로고, 로그인 링크 추가하기
#### ※ 메인페이지로 이동해주는 로고를 가장 왼쪽에 배치하고 오른쪽에는 로그인 링크를 설정 in base.html


##### 2021-02-01
#### 3-02 게시판 페이징 기능 추가하기

#### ※ 페이징을 구현하기 전에 페이징을 테스트할 정도로만 충분한 임시 질문 데이터 300개 생성하기
#### 개인으로 진행한 Seed 데이터로 생성하기

#### 0 pip install django-seed 설치하기
#### 1 config --> settings.py INSTALLED_APPS 안에 django_seed 추가
#### 2 데이터를 넣고자 하는 App 폴더안에 management/commands/seed.py 디렉토리 구성
#### ※ management 폴더안에 __init__.py를 추가하여 Django가 인식할수 있도록하기 (필수)
#### ※ 디렉토리 구성후 management 시스템으로 이용할수 있는 명령어 확인 = python manage.py --help 등록한 seed 내용이 존재하면 Ok
#### 3 seed_board.py 명령어에 대한 argumnet 작성후 handle 로직 까지 구성하면 성공 Git 참조

#### https://github.com/ksm0207/django_pybo/commit/4deed98d56738efeb9169b297cb6f60c48c51ae5

#### page = request.GET.get('page', '1')은 다음과 같은 GET 방식 요청 URL에서 page값을 가져올 때 사용한다.
#### [GET 방식 요청 URL 예]
#### localhost:8000/pybo/?page=1

#### get('page', '1')에서 '1'은 /pybo/ URL처럼 page 파라미터가 없는 URL을 위해 기본값으로 1을 지정한 것이다.
#### 페이징 구현에 사용한 클래스는 Paginator이다.

#### paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여 주기
#### page_obj = paginator.get_page(page)
#### Paginator 클래스는 question_list를 페이징 객체 paginator로 변환한다.
#### 두 번째 파라미터인 10은 페이지당 보여줄 게시물 개수를 의미한다.
#### page_obj = paginator.get_page(page)로 만들어진 page_obj 객체에는 다음과 같은 속성들이 있다.

#### 항목	                설명
#### paginator.count	    전체 게시물 개수
#### paginator.per_page	페이지당 보여줄 게시물 개수
#### paginator.page_range   페이지 범위
#### number	             현재 페이지 번호
#### previous_page_number 이전 페이지 번호
#### next_page_number	 다음 페이지 번호
#### has_previous	     이전 페이지 유무
#### has_next	         다음 페이지 유무
#### start_index	         현재 페이지 시작 인덱스(1부터 시작)
#### end_index	         현재 페이지의 끝 인덱스(1부터 시작)

#### ※ Paginator의  속성들은 템플릿에서 페이징을 처리할 때 사용된다.
#### https://github.com/ksm0207/django_pybo/commit/fd0ad1b07c2649f7a215e8d2fbadf7e58a15c2dc

##### 3-02 게시판 페이징 기능 추가하기

#### [1] 게시물 번호 공식 만들기
#### 일련번호 = 전체 게시물 개수 - 시작 인덱스 - 현재 인덱스 + 1

#### ※ 페이지를 역순(최신순)으로 표시해야할때 

#### 전체 개시물 개수 = 게시물 개수
#### 시작 인덱스 = 페이지당 시작되는 게시물 시작 번호 ( ex 1 2 3 ... 10)
#### 현재 인덱스 = 페이지에 보여지는 게시물 개수 만큼 0부터 1씩 증가되는 번호

#### ex ) 전체 게시물 개수 = 12 이고 페이지당 10개씩 게시물을 보여준다면?

#### 1page = 12 - 1 - 0~9 + 1 일때 12번째 에서 3번째 게시물이고
#### 2page = 12 - 11 0~1 +1 일때 2번쨰에서 1번째 게시물 이다

#### 템플릿에서 이 공식을 적용하려면 빼기 기능이 필요하다. 앞에서 더하기 필터(|add:5)를 사용한 것처럼 빼기 필터(|sub:3)가 있으면 좋을 것 같다.
#### 하지만 장고에는 빼기 필터가 없기 때문에 템플릿 필터를 만들어줘야 한다
#### ※ |add:-3와 같이 숫자를 직접 입력하면 더하기 필터를 이용하여 원하는 값을 뺀 결과를 화면에 보여줄 수는 있다.
####   하지만 이 방법은 이곳에는 사용할 수 없다. 왜냐하면 더하기 필터에는 변수를 적용할 수 없기 때문이다.

#### ※ add 필터는 인수로 숫자만 가능하다.

#### [2] 템플릿 필터 디렉터리 만들기

#### 템플릿 필터 함수는 템플릿 필터 파일을 작성한 다음에 정의해야 한다. 템플릿 필터 파일은 템플릿 파일이나 스태틱 파일과 마찬가지로
#### 새로운 디렉토리를 만들어 저장하고 사용해야한다
#### ※ pybo/templatetags/filter.py

#### [3] 템플릿 필터 작성하기

#### 필터에 적용할 파일을 만들고 이 안에는 템플릿 필터 함수를 만든다
#### 템플릿 필터 함수를 만드는 방법은 함수명에 @register.filter라는 애너테이션을 적용하면 템플릿에서 해당 함수를 필터로 사용할 수 있게 된다
#### 지금 만든 템플릿 필터 함수 는 기존 값 value에서 입력으로 받은 값 arg를 빼서 반환할 것이다.

#### [4] 템플릿 필터 사용하기
#### 템플릿 필터를 사용하려면 템플릿 파일 맨 위에 {% load pybo_filter %}와 같이 템플릿 필터 파일을 로드해야 한다. 

#### [5] 공식적용
#### 일련번호 공식은 전체 게시물 개수 - 시작 인덱스 - 현재 인덱스 + 1 이다.

#### 변수.paginator.count	전체 게시물 개수
#### 변수.start_index	    시작 인덱스(1부터 시작)
#### forloop.counter0	    루프 내의 현재 인덱스(forloop.counter0는 0부터, forloop.counter는 1부터 시작)

##### 2021-02-02
#### 3-05 로그인 & 로그아웃 구현하기

#### 장고는 로그인 · 로그아웃을 쉽게 구현할 수 있도록 django.contrib.auth 앱을 제공한다.
#### 이 앱은 장고 프로젝트 생성 시 mysite/config/settings.py에 자동으로 추가된다.

#### [1] common 앱 생성하기

#### [2] 설정 파일에 common 앱 등록하기
#### config/settings.py 파일에 common 앱을 등록하기.

#### ※ settings.py (INSTALLED_APPS 앱 등록) ->  config -> urls.py -> common URL 등록 -> common --> urls.py 생성 -> URL 설정

#### 로그인 구현하기

#### [1] 내비게이션바 수정하고 URL 매핑 추가

#### urls.py = path('login/', auth_views.LoginView.as_view(), name='login')
#### 로그인 기능은 django.contrib.auth 앱을 사용할 것이므로 common/views.py 파일은 수정할 필요가 없고
#### django.contrib.auth 앱의 LoginView 클래스를 사용한다

#### django.contrib.auth 앱의 LoginView 클래스는 다음과 같이 사용한다
#### 첫번째 에러 : 로그인 클릭 시 registration 이라는 템플릿 디렉터리에서 login.html 파일을 찾는 오류 발생
#### 해결방안 : 로그인은 common 앱에 구현할 것이므로 오류 메시지에 표시한 것처럼 registration 디렉터리에 템플릿 파일을 생성하기보다는
####            common 디렉터리에 템플릿을 생성하였다
####            이를 위해 LoginView가 common 디렉터리의 템플릿을 참조할 수 있도록 common/urls.py 파일을 다음과 같이 수정해준다

#### ☆ urls.py =  path('login/', auth_views.LoginView.as_view(), name='login') 개선전
#### ★ urls.py =  path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login') 개선후

#### ※ as_view 함수에 template_name으로 'common/login.html'을 설정하면 registration 디렉터리가 아닌 common 디렉터리에서 login.html 파일을 참조하게 된다
#### ※ templates 폴더안에 common 폴더 생성후 login.html 생성하기 즉 참조할수 있게 만들기

#### [2] 로그인 성공 시 이동할 페이지 등록하기
#### 로그인 성공 시 / 페이지로 이동할 수 있도록 config/settings.py 파일을 수정해주었다
#### LOGIN_REDIRECT_URL을 추가 :: LOGIN_REDIRECT_URL = '/'

#### [3] 로그아웃 구현하기
#### {% if user.is_authenticated %}
####     <a class="nav-link" href="{% url 'common:logout' %}">{{ user.username }} (로그아웃)</a>
#### {% else %}
####     <a class="nav-link" href="{% url 'common:login' %}">로그인</a>
#### {% if user.is_authenticated %}은 현재 로그인 상태를 판별하여 로그인 상태라면 로그아웃 링크를, 로그아웃 상태라면 로그인 링크를 보여 준다

#### [4] 로그아웃 URL 매핑하기
#### 로그아웃 링크가 추가되었으므로 {% url 'common:logout' %}에 대응하는 URL 매핑을 common/urls.py 파일에 추가하자.
#### path('logout/', auth_views.LogoutView.as_view(), name='logout'),

#### [5] 로그아웃 성공 시 이동할 페이지 등록하기
#### 로그인 성공 시 리다이렉트할 위치인 LOGIN_REDIRECT_URL을 등록했던 것과 마찬가지로 로그아웃 성공 시 리다이렉트할 위치도 config/settings.py 파일에 추가하자
#### LOGOUT_REDIRECT_URL = '/'


##### 2021-02-05
#### 3-06 회원가입 구현하기
#### GitHub : https://github.com/ksm0207/django_pybo/commit/f0b8c5a3afb1f282d255c26b2f433073f5bd28af

#### ※ 장고의 django.contrib.auth 앱을 이용하여 구현시작
#### ※ 내가 생각한 View를 만들기 위한 절차 단계

#### [1] 회원가입 링크 추가
#### ※ login.html 파일에 다음과 같이 URL을 만들어준다
#### <span>또는 <a href="{% url 'common:signup' %}">계정을 만드세요.</a></span>

#### [2] 회원가입 URL 매핑 추가하기
#### common:signup 으로 이동 할수 있도록 urls.py에 매핑을 추가해주자
#### path('signup/', views.signup, name='signup'),

#### [3] 회원가입에 필요한 Form 만들기
#### 사용한 Form : UserForm은 django.contrib.auth.forms 패키지의 UserCreationForm 클래스를 상속하고 email 속성을 추가했다.

#### 상속한 UserCreationForm은 다음 속성을 가지고 있다.

#### 속성명	       설명
#### username	 사용자이름
#### password1	 비밀번호1
#### password2	 비밀번호2(비밀번호1을 제대로 입력했는지 대조하기 위한 값)
#### ↑ UserCreationForm이 기본적으로 가지고 있는 속성
#### ※ 위 속성에 부가 정보인 Email 속성을 추가하기 위해서 UserCreationForm을 상속한 UserForm을 만든 것
#### # UserCreationForm 의 is_vaild 함수는 회원가입 화면의 필드값 3개가 모두 입력 되었는지 규칙에 맞는지 검사한다

#### [4] 회원가입을 위한 signup 함수 정의하기
#### POST 요청인 경우 화면에서 입력한 데이터로 새로운 사용자를 생성하고,
#### GET 요청인 경우 common/signup.html 화면을 반환한다.
#### POST 요청에서 form.cleaned_data.get 함수는 회원가입 화면에서 입력한 값을 얻기 위해 사용하는 함수이다
#### 로그인 시 필요한 아이디, 비밀번호를 얻기 위해 사용되었다. 그리고 회원가입이 완료된 이후에 자동으로 로그인되도록 authenticate 함수와 login 함수를 사용했다
#### ※ authenticate, login 함수는 django.contrib.auth 패키지에 있는 함수로 사용자 인증과 로그인을 담당한다

#### [5] 회원가입 템플릿 만들기
#### https://github.com/ksm0207/django_pybo/commit/f0b8c5a3afb1f282d255c26b2f433073f5bd28af#diff-f3d2875723b455f8d58cfd98b636814d22f6d574f6ad0ebe5ef07a67b59d89dd

##### 2021-02-05
#### 3-07 글쓴이 추가하기
### GitHub : https://github.com/ksm0207/django_pybo/commit/d7652b22a61f86fd814e68af083ee505fc4ec907
#### [1] Question 모델에 author 필드 추가하기
#### author = models.ForeignKey(User, on_delete=models.CASCADE)

#### ※ User 모델의 필수 속성

####  속성	      설명
#### username	사용자명
#### password	비밀번호
#### User 모델에는 필수 속성외에도 여러 속성이 있다. 자세한 내용은 다음 URL을 참고하자.

#### https://docs.djangoproject.com/en/3.1/ref/contrib/auth/#django.contrib.auth.models.User

#### [2] makemigrations 명령 실행하고 author 필드 추가 문제 해결하기
#### 모델을 수정했으므로 makemigrations 명령과 migrate 명령을 실행해보면 명령 프롬포트에 다음과 같은 메시지가 나온다

#### You are trying to add a non-nullable field 'author' to question without a default; we can't do that 
#### (the database needs something to populate existing rows).
#### Please select a fix:
#### 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
#### 지금 일회성 기본값 제공 (이 열에 대해 null 값이있는 모든 기존 행에 설정 됨)
#### 2) Quit, and let me add a default in models.py
#### 종료하고 models.py에 기본값을 추가하겠습니다.
#### Select an option: 

#### Question 모델에 author 필드를 추가하면 이미 등록되어 있던 게시물에 author 필드에 해당되는 값이 저장되어야 하는데,
#### 장고는 author 필드에 어떤 값을 넣어야 하는지 모르기 때문이다
#### 즉 기존에 저장된 Question 모델 데이터에는 author 필드값으로 어떤 값을 저장해야 하는지 묻는 것

#### 문제를 해결하는 방법에는 2가지가 있다
#### 첫 번째 방법은 author 필드를 null로 설정하는 방법
#### 두 번째 방법은 기존 게시물에 추가될 author 필드의 값에 강제로 임의 계정 정보를 추가하는 방법
#### 질문, 답변에는 author 필드값이 무조건 있어야 하므로 두 번째 방법을 사용하고 Select an option : 1 을 입력한다
#### 명령 프롬프트에 다시 1을 입력하게 되면 makemigrations 가 완료가 된다

#### ※ 입력한 '1'은 최초 생성했던 슈퍼 유저의 id값이므로 기존 게시물의 author에는 슈퍼 유저가 등록될 것
#### makemigrations 진행 후 migrate(DB) 적용

#### Answer 모델 수정하기

#### [3] Answer 모델에 author 필드 추가하고 문제 해결하기
#### Answer 모델도 위와 동일한 방법으로 똑같이 적용해준다

#### ※ author 필드에 null 값 허용하기
#### author 필드에 null을 허용하면 기존 게시물의 author 필드가 추가될 때 값이 없어도 작동 된다

#### 글쓴이 표시하기
#### ※ 이제 질문 / 답변 모델에 author 필드가 추가 되었으므로 순차적으로 진행한다
#### 먼저 질문 등록시에 author 필드를 추가하도록 하자
#### 질문 답변에 글쓴이를 추가한다는 느낌

#### [4] 답변 등록 함수 수정하기
#### answer.author = request.user
#### 답변 글쓴이는 현재 로그인한 계정이므로 answer.author = request.user로 처리한다
#### (request.user 는 현재 로그인한 계정의 User 모델 객체)

#### [5] 질문 등록 함수 수정하기
#### 이 함수도 마찬가지 방법으로 수정해준다

#### 로그인이 필요한 함수 설정하기

#### [6] 로그아웃 상태에서 질문, 답변 등록해 보기
#### 로그아웃 상태에서 질문 또는 답변을 등록하면 다음과 같은 ValueError 오류가 발생했다

#### 이 오류는 request.user가 User 객체가 아닌 AnonymousUser 객체라서 발생한 것
#### 조금 더 자세히 설명하자면 request.user에는 로그아웃 상태이면 AnonymousUser 객체이고
#### 로그인 상태이면 User 객체가 들어있는데
#### 조금전 author 필드를 정의할 때 User를 이용하도록 했다.
#### 그래서 answer.author = request.user에서 User 대신 현재 AnonymousUser가 대입되어 오류가 발생한 것

#### [7] 오류해결 / 로그인이 필요한 함수에 @login_required 적용하기
#### 이 문제를 해결하려면 로그인이 필요한 함수 answer_create, question_create에 @login_required 애너테이션을 사용해야 한다
#### ※ from django.contrib.auth.decorators import login_required
#### 함수명 위에 @login_required(login_url='common:login') 작성

#### 답변 함수와 질문 함수는 request.user를 포함하고 있으므로 @login_required 애너테이션을 통해
#### 로그인이 되었는지 "우선" 검사하여 오류 발생을 방지해주도록 한다
#### 만약 로그아웃 상태에서 애너테이션이 적용된 함수가 호출되면 자동으로 로그인 화면으로 이동하게 된다
#### 로그인으로 이동할수 있는 이유는 login_url= "common:login" 덕에 이동 할수 있게 되는것이다

#### [8] URL next 인자로 로그인 성공 후 이동할 URL 지정하기
#### 질문 등록하기'를 눌러 로그인 화면으로 전환된 상태에서 웹 브라우저 주소창의 URL을 보면 next 파라미터가 있을 것이다
#### ※ 이는 로그인 성공 후 next 파라미터에 있는 URL로 페이지를 이동해야 한다는 의미 이지만 지금은 그렇게 되고 있지 않다

#### [9] 로그인 템플릿에 hidden 항목 추가하여 next 파라미터 활용하기
#### 로그인 후 next 파라미터에 있는 URL로 페이지를 이동하려면 로그인 템플릿에 다음과 같이 hidden 항목 next를 추가해야 한다.
#### login.html <input type="hidden" name="next" value="{{ next }}">  <!-- 로그인 성공후 이동되는 URL -->
#### ※ 로그인 후 next 파라미터의 URL로 이동

#### [10] 로그아웃 상태에서 아예 글을 작성할 수 없게 만들기
#### 로그아웃 상태에서 아예 답변을 작성할 수 없도록 만드는 방법은 disabled 속성을 사용하는 것이다.
#### detail.html 에서 다음 코드를 추가하여 수정하였다
####              <textarea {% if not user.is_authenticated %}disabled{% endif %}
####              name="content" id="content" class="form-control" rows="10"></textarea>

