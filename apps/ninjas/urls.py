from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^ninjas$', views.ninjas),
    url(r'^ninjas/blue$', views.blue),
    url(r'^ninjas/orange$', views.orange),
    url(r'^ninjas/red$', views.red),
    url(r'^ninjas/purple$', views.purple),
    url(r'^ninjas/(?P<hackerurl>)', views.invalid),
]