from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from photos.api import PhotoViewSet

from photos.views import HomeView, DetailView, CreateView, PhotoListView, UserPhotosView
from rest_framework.routers import DefaultRouter
from users.api import UserViewSet
from users.views import LoginView, LogoutView


# APIRouter
router = DefaultRouter()
router.register(r'api/1.0/photos', PhotoViewSet)
router.register(r'api/1.0/users', UserViewSet, base_name='user')


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Photos URLs
    url(r'^$', HomeView.as_view(), name='photos_home'),
    url(r'^my-photos/$', login_required(UserPhotosView.as_view()), name='user_photos'),
    url(r'^photos/$', PhotoListView.as_view(), name='photos_list'),
    url(r'^photos/(?P<pk>[0-9]+)$', DetailView.as_view(), name='photo_detail'),
    url(r'^photos/new$', CreateView.as_view(), name='create_photo'),

    # API URLs
    url(r'', include(router.urls)),  # incluyo las URLS de API

    # Users URLS
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
]
