from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by=models.ForeignKey(to=User, on_delete=models.PROTECT, null=True, editable=False)
    created_at=models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, editable=False)
    
    class Meta:
        abstract=True

