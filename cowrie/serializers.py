import geoip2
from django.contrib.gis.geoip2 import GeoIP2
from django.core import serializers
from cowrie.models import SSHSession


class SSHSessionSerializer():
    def __init__(self, json_data):
        assert type(json_data) is dict, (
            "'json_data' is of type '{0}', and not dict.".format(type(json_data))
        )

        self.json_data = json_data
        self.valid = False
        self.errors = []

    def is_valid(self):
        """
        One day this method will check if the data provided is valid.
        :return:
        """
        for field in SSHSession._meta.get_fields():
            if field.name == "id": continue
            assert field.name in self.json_data["fields"] or field.blank, (
                "Required field '{0}' not in  data dict.".format(field.name)
            )

        exists = SSHSession.objects.filter(
            session=self.json_data["fields"]["session"],
            sensor=self.json_data["fields"]["sensor"]).first()

        if exists is not None:
            self.errors.append("A session with this session id already exists.")
            return False

        self.valid = True
        return self.valid

    def save(self):
        def dict_get(the_dict, key, default):
            value = the_dict.get(key, default)
            if value is None:
                return default
            return value

        g = GeoIP2()
        gip_data = None
        try:
            gip_data = g.city(self.json_data["fields"]["src_ip"])
        except geoip2.errors.AddressNotFoundError:
            gip_data = {}

        self.json_data["fields"]["country_code"] = dict_get(gip_data, "country_code", "Unknown")
        self.json_data["fields"]["country_name"] = dict_get(gip_data, "country_name", "Unknown")
        self.json_data["fields"]["longitude"] = dict_get(gip_data, "longitude", "Unknown")
        self.json_data["fields"]["latitude"] = dict_get(gip_data, "latitude", "Unknown")
        self.json_data["fields"]["city"] = dict_get(gip_data, "city", "Unknown")

        return SSHSession.objects.create(**self.json_data["fields"])

