from django.shortcuts import render
from django.http import HttpResponse
def welcome(req):
    return HttpResponse("<html><body bgcolor='gold'>\
                        <h2><marquee>welcome to django world</marquee>\
                        <p> hello frame work</p>\
                        </h2></body></html>")
# Create your views here.
