from django.db import models

class Arizalar(models.Model):
    familiya = models.CharField(max_length=200)
    ism = models.CharField(max_length=200)
    sharif = models.CharField(max_length=200)
    telefon = models.CharField(max_length=200)
    pasport_serya = models.CharField(max_length=200)
    pasport_raqam = models.CharField(max_length=200)
    jshr = models.CharField(max_length=200)
    pasport_rasm = models.FileField(upload_to='pasport_rasm/')
    natariyus_pasport = models.FileField(upload_to='pasport_rasm/')
    daraja = models.CharField(max_length=200)
    yonalish = models.CharField(max_length=200)
    diplom_serya_raqam = models.CharField(max_length=200)
    diplom_rasm = models.FileField(upload_to='diplom_rasm/')
    natariyus_diplom = models.FileField(upload_to='diplom_rasm/')
    bitirgan_yil = models.CharField(max_length=200)
    bitirgan_muassasa = models.CharField(max_length=400)
    viloyat = models.CharField(max_length=200)
    tuman = models.CharField(max_length=200)
    kocha = models.CharField(max_length=200)
    rozilik = models.CharField(max_length=200)
    
    
class Yangiliklar(models.Model):
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField()
    rasm = models.FileField(upload_to='yangilik/')
    sana = models.DateTimeField(auto_now_add=True)


