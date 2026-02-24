from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField("projects", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'