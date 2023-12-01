from django.urls import path, include
from .views import main_page,index_page

urlpatterns = [
    path('',main_page),
    path('/exam',index_page,name='exam')

]