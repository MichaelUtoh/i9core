import io
import json
from enum import Enum

from django.http import JsonResponse

from rest_framework import mixins, views, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


# Create your views here.
@api_view()
def index(request):
    data = {
        "slackUsername": "MichaelUtoh",
        "backend": True,
        "age": 30,
        "bio": "I am a backend developer based in Lagos, Nigeria. I love building REST APIs using Python"
    }
    return Response(data)


@api_view(['post'])
def calc(request):
    data = json.loads(request.body)
    res = {}

    if "multiplication" in data['operation_type'].lower():
        res = { 
            "slackUsername": "MichaelUtoh",
            "operation_type": "multiplication",
            "result": f"{data['x'] * data['y']}" }
    elif "addition" in data['operation_type'].lower():
        res = { 
            "slackUsername": "MichaelUtoh",
            "operation_type": "addition",
            "result": f"{data['x'] + data['y']}" }
    elif "subtraction" in data['operation_type'].lower():
        res = { 
            "slackUsername": "MichaelUtoh",
            "operation_type": "subtraction",
            "result": f"{data['x'] - data['y']}" }
    else:
        res = {"detail": "No operation given"}

    return Response(res)






# { “operation_type”: "multiplication" , “x”: 12, “y”: 3 }
# { “slackUsername”: "MichaelUtoh", "operation_type" : action, “result”: res }
class CalcScriptViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    def post(self, request, data=None):
        print("Debug")
        return Response()

