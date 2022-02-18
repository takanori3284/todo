from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.urls import path,include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),
    path('accounts/', include('allauth.urls')),
]

# 開発サーバーでメディアを配信できるようにする設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
