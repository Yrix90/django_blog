from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    text = """<h1>Welcome</h1>"""
    return HttpResponse(text)


def hello2(request, number):
    text = """<h1> welcome2</h1>""" % number
    
