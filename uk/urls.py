"""
Main URL Configuration for UZHAVANKART Project
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # Health check for deployment
    path('health/', lambda request: __import__('django.http', fromlist=['HttpResponse']).HttpResponse('OK')),
    
    # Include all app URLs from uzhavankart app (no prefix - routes already have paths)
    path('', include('uzhavankart.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)