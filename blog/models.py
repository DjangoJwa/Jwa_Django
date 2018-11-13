'''Create your models here.'''
'''
models.CharField - 글자 수가 제한된 텍스트 정의할 때 사용 ex)글 제목
models.TextField - 글자 수에 제한이 없는 긴 텍스트
models.DateTimeField - 날짜와 시간
models.ForeignKey - 다른 모델에 대한 링크
__: 던더
메소드 - space 대신 _
'''

from django.db import models
from django.utils import timezone


class Post(models.Model):
    '''모델(객체)을 정의
    클래스 첫 대문자
    '''
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publih(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
