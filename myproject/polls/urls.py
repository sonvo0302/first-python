from django.urls import path
from django.conf.urls import url
from . import views

app_name= 'polls'
urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^list/$',views.viewlist,name="view_list"),
    # path('list/<int:question_id',views.viewlist,name="view_list"),
    url(r'^list/(?P<pk>[0-9]+)$',views.viewDetail,name="view_detail_list"),
    url(r'^list/new_choice$', views.new_choice, name="new_choice"),
    url(r'^list/(?P<pk>[0-9]+)/vote$',views.vote,name="vote"),
]
