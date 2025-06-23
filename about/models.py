from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class About(models.Model):
    """
    Stores information about the website author.

    Includes profile image, title, content, and last updated date.
    """
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class CollaborateRequest(models.Model):
    """
    Stores a collaboration request submitted by a site visitor.

    Includes name, email, message, and submission time.
    """
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration Request from {self.name}"
