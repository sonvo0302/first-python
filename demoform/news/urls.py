from django.conf.urls import url
from . import views
app_name ='news'
urlpatterns = [
    url(r'^$',views.index.as_view(),name='index'),
    url(r'^add/$',views.PostClass.as_view(),name='add_post'),
    # url(r'^save/$',views.SavePostClass.as_view(),name='save_post'),
    url(r'^email/$',views.emailview,name='email'),
    url(r'^process/$',views.process,name='process'),
    url(r'^list/$',views.PostListClass.as_view(),name='list_post'),
    url(r'^update/(?P<pk>[0-9]+)$',views.PostUpdateClass.as_view(),name='update_post'),
    url(r'^delete/(?P<pk>[0-9]+)$',views.PostDeleteClass.as_view(),name='delete_post'),
]