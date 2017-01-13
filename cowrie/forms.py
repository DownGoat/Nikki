from django import forms

from cowrie.models import SSHSession


class SSHSessionForm(forms.ModelForm):
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)
    password3 = forms.CharField(required=False)

    username1 = forms.CharField(required=False)
    username2 = forms.CharField(required=False)
    username3 = forms.CharField(required=False)

    timestamp = forms.DateTimeField(input_formats=["%Y-%m-%dT%H:%M:%S.%fz"])
    class Meta:
        model = SSHSession
        fields = (
            "session_id",
            "source_ip",
            "source_port",
            "destination_ip",
            "destination_port",
            "sensor",
            "timestamp",
            "password1",
            "password2",
            "password3",
            "username1",
            "username2",
            "username3",
            "macCS",
            "kexAlgs",
            "keyAlgs",
            "encCS",
            "version"
        )
