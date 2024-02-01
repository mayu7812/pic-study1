# main/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studyapp.urls')),  # 'your_app_name' を実際のアプリケーションの名前に変更
    # 他のURLパターンも必要に応じて追加
]
