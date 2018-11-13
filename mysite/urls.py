"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

'''
urlresolver가 사용하는 패턴 목록을 포함함.
'''
'''
#url에서 admin/로 시작하는 모든 URL을 view와 대조하여 찾아낸다. -> 매우 많아 -> 정규식 사용
정규식(raw string)
^ - 문자열 시작
$ - 문자열 끝
() - 패턴 부분 정할때(그룹핑)
'''


from django.conf.urls import include, url
from django.contrib import admin

'''
mysite/urls.py 파일을 깨끗하게 유지하기 위해
blog App에서 메인 mysite/urls.py 파일로 url들을 가져올거임.'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]


