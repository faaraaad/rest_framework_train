from django.urls import path
from . import views
from rest_framework import routers


app_name = 'home'

r1 = routers.SimpleRouter()
r1.register('routertest', views.RouterTestViewset)
urlpatterns =[
    path('home/', views.HomeView.as_view(), name='home'),
    path('test/<str:who>/', views.TestShow.as_view(), name='test'),
    path('account/user/', views.CreateUser.as_view(), name='create_user'),
    path('post/<int:post_id>/', views.PostDetail.as_view(), name= 'post_detail'),
    path('register/', views.RegisterView.as_view())
]

urlpatterns += r1.urls
