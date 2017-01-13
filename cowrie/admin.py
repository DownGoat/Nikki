from django.contrib import admin

# Register your models here.
from cowrie.models import SSHSession

admin.site.register(SSHSession)
