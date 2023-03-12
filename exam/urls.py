from django.urls import re_path as url
from exam import views 

urlpatterns=[
    url('test',views.showTest),
    url('result',views.showResult)
    ]
