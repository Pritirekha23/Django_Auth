from django.db import models
from django.contrib.auth.models import User
import uuid


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50)
    vat_number = models.CharField(max_length=50)
    address = models.TextField()
    role = models.CharField(max_length=50, choices=[
        ('Owner', 'Owner'),
        ('Director', 'Director'),
        ('Finance Manager', 'Finance Manager'),
        ('General Manager', 'General Manager'),
    ])
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"