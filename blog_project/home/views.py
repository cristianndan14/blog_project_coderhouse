from django.shortcuts import redirect, render


def index(request):
    return render(request, template_name="home/main.html")