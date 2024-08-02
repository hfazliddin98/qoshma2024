from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from.views import ariza_yuborish, qabul, qabul_qilindi, magistr, bakalavr, malumot, magistr_csv, bakalavr_csv


urlpatterns = [
    path('ariza_yuborish/', ariza_yuborish, name='ariza_yuborish'),
    path('qabul/', qabul, name='qabul'),
    path('qabul_qilindi/', qabul_qilindi, name='qabul_qilindi'),
    path('bakalavr/', bakalavr, name='bakalavr'),
    path('magistr/', magistr, name='magistr'),
    path('malumot/<int:pk>/', malumot, name='malumot'),
    path('magistr_csv/', magistr_csv, name='magistr_csv'),
    path('bakalavr_csv/', bakalavr_csv, name='bakalavr_csv'),
]

