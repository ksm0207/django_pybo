from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Config --> urls.py 파일은 페이지 요청 시 가장 먼저 호출되며 요청 URL과 View 함수를 1:1로 연결한다
# URL 매핑 --> 페이지 요청 추가하기

# pybo/ 로 시작되는 페이지 요청은 모두 pybo/urls.py 파일에 있는 URL 매핑을 처리된다
urlpatterns = [
    path("admin/", admin.site.urls),
    path("pybo/", include("pybo.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
