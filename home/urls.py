from django.urls import path
from . import views


app_name='home'
urlpatterns=[
    path('home/', views.HomeView.as_view(), name='home'),
    path('test/<str:who>/', views.TestShow.as_view(), name='test'),
    path('account/user/', views.CreateUser.as_view(), name='create_user')
]

