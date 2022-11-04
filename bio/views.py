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
    operation_type = data["operation_type"].lower()

    if operation_type == "multiplication":
        result = data['x'] * data['y']
    elif operation_type == "addition":
        result = data['x'] + data['y']
    elif operation_type == "subtraction":
        result = data['x'] - data['y']
    else:
        response1 = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"{operation_type} in one word",
            temperature=0.3,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        ).choices[0].text.strip()

        response2 = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"{operation_type} operation type in one word",
            temperature=0.3,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        ).choices[0].text.strip()

        return Response({
            "slackUsername": "MichaelUtoh",
            "result": int(response1),
            "operation_type": response2,
        })

    return Response({
        "slackUsername": "MichaelUtoh",
        "operation_type": operation_type,
        "result": result
    })
