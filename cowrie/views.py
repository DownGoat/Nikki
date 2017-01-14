import ujson

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cowrie.serializers import SSHSessionSerializer


@csrf_exempt
def create_session(request):
    if request.method == "POST":
        json_data = ujson.loads(request.body.decode("utf-8"))

        serializer = SSHSessionSerializer(json_data[0])
        if not serializer.is_valid():
            return JsonResponse({"success": False, "msg": serializer.errors})

        serializer.save()

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