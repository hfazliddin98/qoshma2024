from modeltranslation.translator import translator, register, TranslationOptions
from .models import Yangiliklar

@register(Yangiliklar)
class YangilikTarjima(TranslationOptions):
    fields = ('title', 'body')
    


