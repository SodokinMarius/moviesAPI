from django.http import JsonResponse

def ping(request):
    data={"ping":"Bonjour, Bien j'espère !!!"}
    return JsonResponse(data)