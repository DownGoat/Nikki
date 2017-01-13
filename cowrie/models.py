from django.db import models


class SSHSession(models.Model):
    session = models.CharField(max_length=64)
    src_ip = models.CharField(max_length=64)
    src_port = models.IntegerField()
    sensor = models.CharField(max_length=64)
    timestamp = models.DateTimeField("date published")

    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)
    password3 = models.CharField(max_length=128)

    username1 = models.CharField(max_length=128)
    username2 = models.CharField(max_length=128)
    username3 = models.CharField(max_length=128)

    macCS = models.CharField(max_length=1024)
    kexAlgs = models.CharField(max_length=1024)
    keyAlgs = models.CharField(max_length=1024)
    encCS = models.CharField(max_length=1024)
    version = models.CharField(max_length=1024)

    def __str__(self):
        return "SSH {0} - {1} - {2} - {3}".format(self.sensor, self.src_ip, self.username1, self.password1)