from django.db import models


class SSHSession(models.Model):
    session = models.CharField(max_length=64)
    src_ip = models.CharField(max_length=64)
    src_port = models.IntegerField()
    sensor = models.CharField(max_length=64)
    timestamp = models.DateTimeField("date published")

    macCS = models.CharField(max_length=1024)
    kexAlgs = models.CharField(max_length=1024)
    keyAlgs = models.CharField(max_length=1024)
    encCS = models.CharField(max_length=1024)
    version = models.CharField(max_length=1024)

    def __str__(self):
        return "SSH {0} - {1} - {2} - {3}".format(self.sensor, self.src_ip, self.username1, self.password1)


class LoginDetails(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    association = models.CharField(max_length=128)

    def __str__(self):
        return "LoginDetails: {0}:{1} - {2}".format(self.username, self.password, self.association)