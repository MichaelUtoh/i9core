import io
import json
import os
from enum import Enum

from django.http import JsonResponse

import openai
from decouple import config
from rest_framework import mixins, views, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

openai.api_key = config("OPEN_API_KEY")

# Create your views here.
# @api_view()
def index(request):
    data = {
        "slackUsername": "MichaelUtoh",
        "backend": True,
        "age": 30,
        "bio": "I am a backend developer based in Lagos, Nigeria. I love building REST APIs using Python"
    }
    return JsonResponse(data)


# @api_view(['post'])
def calc(request):
    data = json.loads(request.body)
    operation_type = data["operation_type"].lower()

    KEYWORDS = ['add','subtract','multiply','addition', 'sum','subtraction','multiplication', 'product']

    if operation_type == "multiplication":
        result = data['x'] * data['y']
    elif operation_type == "addition":
        result = data['x'] + data['y']
    elif operation_type == "subtraction":
        result = data['x'] - data['y']
    else:
        operation_type = data['operation_type']
        operation_type_list = operation_type.split()
        x = int(data['x'])
        y = int(data['y'])

        operation = [item for item in operation_type_list if item in KEYWORDS][0]
        if operation:

            if operation ==  'add' or operation ==  'addition':
                operation_type = 'addition'
                result = x + y
            elif operation ==  'subtract' or operation == 'subtraction':
                operation_type = 'subtraction'
                result = x - y
            elif operation ==  'multiplication' or operation == 'multiply' or operation== 'product':
                operation_type = 'multiplication'
                result = x * y

        return JsonResponse({
            "slackUsername": "MichaelUtoh",
            "result": operation_type,
            "operation_type": result,
        })

    return JsonResponse({
        "slackUsername": "MichaelUtoh",
        "operation_type": operation_type,
        "result": result
    })
