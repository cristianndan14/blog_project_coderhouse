from django.shortcuts import render
from django.db.models import Q


def index(request):
    return render(
        request=request,
        template_name="home/main.html"
    )


