from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('contactos_app.urls')),
    
    
]
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
