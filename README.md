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




