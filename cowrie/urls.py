from django.conf.urls import url
from .views import create_session


app_name = "cowrie"

urlpatterns = [
    url(r'^event$', create_session, name='Create Event'),
]