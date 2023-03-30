from django.urls import path
from . import views

urlpatterns = [
    path('bacias/', views.bacias_view, name='bacias'),
]