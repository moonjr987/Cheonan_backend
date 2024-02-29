from django.urls import path
from django.urls.conf import include
from django.contrib import admin
from . import views
from .views import CultureBankListCreateAPIView
from .views import store_search
from .views import my_view


urlpatterns = [
    path('', views.index),
    path('register/', views.register, name='register'),
    path('get_register_info/', views.GetUserByCredentialsView.as_view(), name='get_register_info'),
    path('generate_key/', views.GenerateApiKeyView.as_view(), name='generate_key'),
    path('accounts/kakao/login/callback/', views.getUserInfo, name='getUserInfo'),
    path('kakaoGetLogin', views.kakaoGetLogin, name='kakaoGetLogin'),
    path('account/', include('allauth.urls')),
    path('culturebanks/', CultureBankListCreateAPIView.as_view(), name='culturebank_list_create'),
    path('get_culture_banks/', views.get_culture_banks, name='get_culture_banks'),
    path('search/', views.store_search, name='search'),
    path('yeouijus/', views.my_view, name='yeouijus'),
]

