#-*- coding: utf-8 -*-
from django.shortcuts import render
from photos.models import Photo, PUBLIC


def home(request):
    """
    Esta función devuelve el home de mi página
    """
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photos_list': photos[:5]
    }
    return render(request, 'photos/home.html', context)
