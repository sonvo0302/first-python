from django.conf.urls import url
from . import views


app_name='LoginApp'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^login/$',views.LoginClass.as_view(),name='login'),
    url(r'^view/$',views.ViewUser.as_view(),name='view_user'),
    url(r'^view_product/$', views.view_product, name='view_user'),
    url(r'^add_post/$', views.AddPost.as_view(), name='add_post'),
]
#path('detail/<int:question_id>'...)