from django.contrib import admin

# Register your models here.
from cowrie.models import SSHSession, LoginDetails

admin.site.register(SSHSession)
admin.site.register(LoginDetails)
