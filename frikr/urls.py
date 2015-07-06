from django.conf.urls import include, url
from django.contrib import admin

from photos.views import HomeView
from users.views import LoginView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Photos URLs
    url(r'^$', HomeView.as_view(), name='photos_home'),
    url(r'^photos/(?P<pk>[0-9]+)$', 'photos.views.detail', name='photo_detail'),
    url(r'^photos/new$', 'photos.views.create', name='create_photo'),

    # Users URLS
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', 'users.views.logout', name='users_logout')
]
