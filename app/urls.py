from django.urls import path
from .views import *

urlpatterns = [
    path('add/bacia', bacia_create, name='add-bacia'),
    path('bacia/<int:id>', bacia_edit, name='edit-bacia'),
    path('bacias/', bacia_list, name='bacias'),

    path('add/tipo_bacia', tipo_bacia_create, name='add-tipo-bacia'),
    path('tipo_bacia/<int:id>', tipo_bacia_edit, name='edit-tipo-bacia'),
    path('tipo_bacias/', tipo_bacia_list, name='tipo-bacias'),

    path('add/engenheiro', engenheiro_create, name='add-engenheiro'),
    path('engenheiro/<int:id>', engenheiro_edit, name='edit-engenheiro'),
    path('engenheiro/', engenheiro_list, name='engenheiro'),

    path('add/endereco', endereco_create, name='add-endereco'),
    path('endereco/<int:id>', endereco_edit, name='edit-endereco'),
    path('endereco/', endereco_list, name='endereco'),

    path('', gerenciamento, name='gerenciamento'),

    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', logout_view, name='logout'),
]
