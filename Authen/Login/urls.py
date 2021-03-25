from django.conf.urls import url
from . import views

appname='authen'
urlpatterns=[
    url(r'^$',views.IndexClass,name='index'),
    url(r'^login/$',views.LoginClass.as_view(),name='login'),
    url(r'^view/$',views.ViewUser.as_view(),name='view_user'),
    url(r'^view_product/$', views.view_product, name='view_user'),
]
#path('detail/<int:question_id>'...)