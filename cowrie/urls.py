from django.conf.urls import url
from .views import create_session, create_login_details

app_name = "cowrie"

urlpatterns = [
    url(r'^session', create_session, name='Create Event'),
    url(r'^login-details', create_login_details, name='Create Event'),
]