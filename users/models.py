import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    lavozim = models.CharField(max_length=100)
    parol = models.CharField(max_length=100)
