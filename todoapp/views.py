from django.http import JsonResponse


def hello(request):
    return JsonResponse({
        "message": "Hello welcome to todoapp"
    }, status=200)
