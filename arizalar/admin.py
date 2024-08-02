from django.contrib import admin
from .models import Arizalar, Yangiliklar

class Arizalaradmin(admin.ModelAdmin):
    list_display = [
        'id', 'familiya', 'ism', 'sharif'
    ]
    
admin.site.register(Arizalar, Arizalaradmin)

class Yangiliklaradmin(admin.ModelAdmin):
    list_display = [
        'id', 'title'
    ]
    
admin.site.register(Yangiliklar, Yangiliklaradmin)




