from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
# Model 클래스를 상속받음. 쟝고 프로그램의 Model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()
    image = models. ImageField(upload_to='posts', null = True)
    # MEDIA_ROOT/posts/이미지파일명 위치에 저장하겠다.image에 이미지의 경로를 저장하겠다.
    # 게시물을 작성할 때 이미지를 반드시 넣지 않아도 된다.
    created_at = models.DateField()
    liked_users = models.ManyToManyField(User, related_name='liked_posts')
    #author = models.CharField(max_length=100)
            ## 짧은 문장을 의미하는 CharField 글자제한 넣을 수 있음
    #body = models.TextField()
            ## TextField 장문을 넣을 수 있음.
    #created_at = models.DateTimeField()
# 쟝고 Model Field 를 구글에 검색하면 다양하게 나옴
    def __str__(self):
        #__str__ 메소드 : 기존에있던 던덜스트링메쏘드를 덮어쓰기한것
        #작성자 : 본문을 프린트하게 만듬
        if self.user:
            return f'{self.user.get_username()}: {self.body}'
            #return 코드는 다시 위로 돌아가게 만드는 코드, else를 적을 필요가 없음.
        return f'{self.body}'