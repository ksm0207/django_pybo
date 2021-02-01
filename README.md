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
#### 2 데이터를 넣고자 하는 App 폴더안에 management/commands/seed.py 구성
#### ※ management 폴더안에 __init__.py를 추가하여 Django가 인식할수 있도록하기 (필수)
#### ※ 디렉토리 구성후 management 시스템으로 이용할수 있는 명령어 확인 = python manage.py --help 등록한 seed 내용이 존재하면 Ok
#### 3 seed_board.py 명령어에 대한 argumnet 작성후 handle 로직 까지 구성하면 성공 Git 참조

