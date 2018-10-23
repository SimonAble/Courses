from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^remove/(?P<number>\d+)$', views.remove),
    url(r'^confirm_remove$', views.confirm_remove)
]