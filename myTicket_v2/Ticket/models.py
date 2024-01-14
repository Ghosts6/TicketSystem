from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Custom User Profile 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.user.username

# Model to represent tickets 
class Ticket(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Closed', 'Closed'),  
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    request_type = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    attachment = models.FileField(upload_to='ticket_attachments/', blank=True, null=True) 

    def __str__(self):
        return f"Ticket - {self.name} {self.last_name} ({self.department_name})"


# Admin model f
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

