from django.urls import re_path as url
from BRMapp import views 

urlpatterns=[
    url('edit-book',views.editBook),
    url('new-book',views.newBook),
    url('view-book',views.viewBooks),
    url('search-book',views.searchBook),
    url('delete-book',views.deleteBook),
    url(r'^add',views.add),
    url('edit',views.edit),
    url('search',views.search),
    url('login',views.userLogin),
    url('logout',views.userLogout),
    url('^$',views.userLogin),
    ]
