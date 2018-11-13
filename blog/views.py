'''
Create your views here
your App - logic here
M모델에서 필요한 정보를 받아와서 T템플릿에 전달하는 역할'''


from django.shortcuts import render

def post_list(request):
    #호출하여 받은 return 템플릿을 보여줌
    return render(request, 'blog/post_list.html', {})

