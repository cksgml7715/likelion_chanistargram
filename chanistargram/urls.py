"""chanistargram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# from posts import views  posts를 views로 처리하겠다는 의미
# 쟝고서버가 기다리다가 누가 포스츠를 요청했을때 뷰즈인덱스를 실행함. 내부적으로
# 그래서 굳이 괄호를 열고닫지 않음

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('posts/', views.index, name= 'index'),
    path('posts/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      # http://www.heeham.com/media/이미지파일명 과 같은 접근이 가능하게 해줍니다.(development only)

