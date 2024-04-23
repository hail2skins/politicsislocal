from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
# Model class for InvitationCode.
# This model will be used to store the invitation codes to integrate with the registration form.
class InvitationCode(models.Model):
    code = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.code
