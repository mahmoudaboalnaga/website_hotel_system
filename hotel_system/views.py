from django.http import HttpResponse

def WelcomePage(request):
    return HttpResponse("This is the welcome page")