#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC
from django.contrib.auth.decorators import login_required
from django.views.generic import View


class HomeView(View):

    def get(self, request):
        """
        Esta función devuelve el home de mi página
        """
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
        context = {
            'photos_list': photos[:5]
        }
        return render(request, 'photos/home.html', context)


def detail(request, pk):
    """
    Carga la página de detalle de una foto
    :param request: HttpRequest
    :param pk: id de la foto
    :return: HttpResponse
    """
    """
    También podemos utilizar esta sintaxis de recuperació de un objeto:
    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        photo = None
    except Photo.MultipleObjects:
        photo = None
    """
    possible_photos = Photo.objects.filter(pk=pk).select_related('owner')
    # photo = (possible_photos.lenght == 1) ? ossible_photos[0] : null;
    photo = possible_photos[0] if len(possible_photos) >= 1 else None
    if photo is not None:
        # cargar la plantilla de detalle
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound('No existe la foto')  # 404 not found


@login_required()
def create(request):
    """
    Muesta un formulario para crear una foto y la crea si la petición es POST
    :param request: HttpRequest
    :return: HttpResponse
    """
    success_message = ''
    if request.method == 'GET':
        form = PhotoForm()
    else:
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user  # asigno como propietario de la foto, el usuario autenticado
        form = PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save()  # Guarda el objeto Photo y me lo devuelve
            form = PhotoForm()
            success_message = 'Guardado con éxito!'
            success_message += '<a href="{0}">'.format(
                reverse('photo_detail', args=[new_photo.pk])
            )
            success_message += 'Ver foto'
            success_message += '</a>'

    context = {
        'form': form,
        'success_message': success_message
    }
    return render(request, 'photos/new_photo.html', context)
































