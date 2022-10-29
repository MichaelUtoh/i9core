from django.http import JsonResponse

# Create your views here.
def index(request):
    data = {
        "slackUsername": "Michael Utoh",
        "backend": True,
        "age": 30,
        "bio": "I am a backend developer based in Lagos, Nigeria. I love building REST APIs using Python"
    }
    return JsonResponse(data)