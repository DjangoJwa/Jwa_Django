from django.conf.urls import url
from .import views
''' 장고의 메소드url과 blog-app에서 사용할 모든 views를 불러옴'''


urlpatterns = [
    url(r'^$', views.post_list, name='post_list')
]
'''post_list라는 이름의 view가 ^$ URL에 할당 됬다. 
이는 정규식이 ^시작해서 $ 끝남을 알림 -> 문자열이 아무것도 없는경우(^$)
장고에게 누군가 웹사이트에 127.0.0.1.:8000 주소로 들어왔을 때
view.post_list를 보여주게됨.
초기 - 장고가 사용하려고 하는 뷰가 아직 없음'''

