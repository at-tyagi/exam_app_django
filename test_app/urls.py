from django.urls import re_path as url
from test_app import views

urlpatterns=[
    url('about',views.about),
    url('contact',views.showContact),
    url('employee',views.employee_info_view),
    url('^$',views.greeting)
    ]
