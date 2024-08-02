from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('haker/', admin.site.urls), 
    path('', include('django.contrib.auth.urls')),       
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),   
    path('', include('users.urls')),
    path('arizalar/', include('arizalar.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
