# django_pybo
# Python Web 프로그래밍 학습시작 
# 출처 https://wikidocs.net/book/4223

# Todo List

# 2021-01-14 
# [] Model 만들기
# [] 질문 목록 및 질문 상세 기능 구현하기

# Filter VS GET 

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

[1] pybo/urls.py 수정하여 URL 별칭 사용하기
    템플릿의 href에 실제 주소가 아니라 URL 별칭을 사용하려면 우선 pybo/urls.py 파일을 수정해야 한다.
    path 함수에 있는 URL 매핑에 name 속성을 부여하자.
    path('', views.index, name='index'), index 라는 URL 별칭 만들기
    path('<int:question_id>/', views.detail, name='detail'), detail 이라는 URL 별칭이 생김

[2] pybo/question_list.html 템플릿에서 URL 별칭 사용하기
    1단계에서 만든 별칭을 템플릿에서 사용하기 위해 /pybo/{{ question.id }}를 {% url 'detail' question.id %}로 변경하자.
    question.id는 URL 매핑에 정의된 <int: question_id>를 의미한다.

URL 네임스페이스 알아보기
여기서 한 가지 더 생각할 문제가 있다. 현재의 프로젝트에서는 pybo 앱 하나만 사용하지만
이후 pybo 앱 이외의 다른 앱이 프로젝트에 추가될 수도 있다. 이때 서로 다른 앱에서 같은 URL 별칭을 사용하면 중복 문제가 생긴다.
이 문제를 해결하려면 pybo/urls.py 파일에 네임스페이스(namespace)라는 개념을 도입해야 한다. 네임스페이스는 쉽게 말해 각각의 앱이 관리하는 독립된 이름 공간을 말한다.
사용방법은 urls.py 파일에 간단히 app_name 변수에 네임스페이스 이름을 저장하면 된다.