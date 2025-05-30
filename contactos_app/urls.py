from django.urls import path
from .views import ContactoViewSet
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('contactos',ContactoViewSet, basename='contactos')
urlpatterns= router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
