from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from files.api import FileViewSet


# APIRouter
router = DefaultRouter()
router.register(r'files', FileViewSet)


urlpatterns = [
    # API URLs
    url(r'1.0/', include(router.urls)),  # incluyo las URLS de API
]
