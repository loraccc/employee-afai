from django.urls import path,include
from . import views
urlpatterns = [
    path('login',views.login_user , name='login'),
    path('',views.INDEX,name='index'),
    path('add',views.ADD,name='add'),
]
