from django.urls import path
from .views import home, kirish, superadmin_qoshish


urlpatterns = [
    path('', home, name='home'),
    path('admin/kirish/', kirish, name='kirish'),
    path('admin/royhat/', superadmin_qoshish, name='admin_qoshish')
]