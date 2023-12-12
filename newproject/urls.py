from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.urls import re_path  # Import re_path for regular expression-based URL patterns
from django.conf.urls.static import static  # Import static for serving static files during development
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newapp.urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)