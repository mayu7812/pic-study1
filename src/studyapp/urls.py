# main/urls.py

from django.urls import path
from .views import some_async_view

urlpatterns = [
    path('some_async_view/', some_async_view, name='some_async_view'),
    # 他のURLパターンを追加する場合はここに記述
]
