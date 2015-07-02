#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo


def home(request):
    """
    Esta función devuelve el home de mi página
    """
    photos = Photo.objects.all()
    html = '<ul>'
    for photo in photos:
        html += '<li>' + photo.name + '</li>'
    html += '</ul>'
    return HttpResponse(html)
