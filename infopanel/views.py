import geoip2
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
from django.contrib.gis.geoip2 import GeoIP2
# Create your views here.
from cowrie.models import SSHSession


def index(request):
    return render(request, "infopanel/index.html")


def latest_sessions(request, pk):
    sessions = None
    if pk == "0":
        sessions = SSHSession.objects.all().order_by('-id')[:50]
        #sessions = SSHSession.objects.all()
    else:
        sessions = SSHSession.objects.filter(id__gt=pk)
    json_data = []
    g = GeoIP2()
    for session in sessions:
        try:
            gip_data = g.city(session.src_ip)

            session_json = {
                "id": session.id,
                "country_code": gip_data.get("country_code"),
                "country_name": gip_data.get("country_name"),
                "longitude": gip_data.get("longitude"),
                "latitude": gip_data.get("latitude"),
                "city": gip_data.get("city"),
                "src_ip": session.src_ip,
                "timestamp": session.timestamp,
                "type": "SSH Brute",
            }
            json_data.append(session_json)
        except geoip2.errors.AddressNotFoundError:
            pass

    return JsonResponse({"success": True, "data": json_data})