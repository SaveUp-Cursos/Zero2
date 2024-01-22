# backend/core/models.py
from django.db import models

class Cliente(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    class Meta:
        app_label = 'core'
