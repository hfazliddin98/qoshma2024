from django.urls import path
from .views import home, kirish, superadmin_qoshish, chiqish


urlpatterns = [
    path('', home, name='home'),
    path('logout/', chiqish, name='logout'),
    path('admin/kirish/', kirish, name='kirish'),
    path('admin/royhat/', superadmin_qoshish, name='admin_qoshish')
]