from django.db import models

from core.models import BaseModel


class Note(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
