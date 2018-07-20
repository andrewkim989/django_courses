from django.conf.urls import url
from . import views   

urlpatterns = [
    url(r'^$', views.courses),
    url(r'^courses/create$', views.add_process),
    url(r'^courses/(?P<num>\d+)/delete$', views.delete),
    url(r'^courses/(?P<num>\d+)/delete_process$', views.delete_process),
    url(r'^courses/(?P<num>\d+)/add$', views.add),
    url(r'^courses/add_comment$', views.add_comment)
]