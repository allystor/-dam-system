from django.urls import path
from .views import bacias_view, BaciaList

urlpatterns = [
    path('bacias/', bacias_view, name='bacias'),
    path('bacias_api/', BaciaList.as_view(), name='bacias_api'),
]