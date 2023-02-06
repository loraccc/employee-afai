from django.urls import path,include
from . import views
from .views import (EmployeeApiview,EmpIDApiview)
urlpatterns = [
    path('login',views.login_user , name='login'),
    path('',views.INDEX,name='index'),
    path('base',views.Base,name='base'),
    path('add',views.ADD,name='add'),
    path('edit/<str:id>',views.EDIT,name='edit'),   
    path('update/<str:id>',views.UPDATE,name='update'), 
    path('delete/<str:id>',views.DELETE,name='delete'), 

    #api
    path('api/emp/',EmployeeApiview.as_view()),
    path('api/emp/<int:id>/',EmpIDApiview.as_view())



]
