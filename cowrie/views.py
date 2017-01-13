import ujson

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

import cowrie
from cowrie.models import SSHSession


@csrf_exempt
def create_session(request):
    if request.method == "POST":
        json_data = request.body.decode("utf-8")

        resultJson = serializers.deserialize('json', request.body)

        for obj in resultJson:
            exists = SSHSession.objects.filter(session=obj.object.session, sensor=obj.object.sensor).first()
            if exists is not None:
                return JsonResponse({"success": False, "msg": "Session already exists in our database."})
            obj.save()

        return JsonResponse({"success": True})
    else:

        return JsonResponse({"success": True})


@csrf_exempt
def create_login_details(request):
    if request.method == "POST":
        json_data = request.body.decode("utf-8")
        resultJson = serializers.deserialize('json', request.body)

        for obj in resultJson:
            obj.save()

        return JsonResponse({"success": True})
    return JsonResponse({"success": True})