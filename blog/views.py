'''
Create your views here
모델-(뷰)연결-템플릿
your App - logic here
M모델에서 필요한 정보를 받아와서 T템플릿에 전달하는 역할
템플릿이란 서로 다른 정보를 일정한 형태로 표시하기 위해 재사용 가능한 파일을 만듦
Django - HTML
'''


from .models import Post
#현재 디렉토리 또는 어플리케이션 동일 디렉토리 내 있기 때문에
from django.shortcuts import render
from django.utils import timezone

def post_list(request):
    #호출하여 받은 return 템플릿을 보여줌

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts는 쿼리셋의 이름


    return render(request, 'blog/post_list.html', {'posts': posts})
    #render함수에는 매개변수 request와 템플릿post_list.html 존재

