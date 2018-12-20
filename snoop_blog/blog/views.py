from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Post,Comment

# Create your views here.

def index(request):
    output={"Primera vista snoop_blog"}
    return HttpResponse(output)
