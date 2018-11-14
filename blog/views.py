'''
Create your views here
your App - logic here
M모델에서 필요한 정보를 받아와서 T템플릿에 전달하는 역할
템플릿이란 서로 다른 정보를 일정한 형태로 표시하기 위해 재사용 가능한 파일을 만듦
Django - HTML
'''


from django.shortcuts import render

def post_list(request):
    #호출하여 받은 return 템플릿을 보여줌
    return render(request, 'blog/post_list.html', {})

