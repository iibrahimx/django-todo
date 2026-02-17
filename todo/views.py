from django.http import HttpResponse
from django.shortcuts import render


def addTask(request):
    return HttpResponse("The form is submitted")
