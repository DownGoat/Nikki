from django.conf.urls import url
from . import views

app_name = "infopanel"
urlpatterns = [
    url(r'^$', views.index, name="Infopanel Index"),
    url(r'^latest/(?P<pk>[^/]+)/$', views.latest_sessions, name="Infopanel Index"),
]