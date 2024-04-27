from django.db import models
from django.core.validators import FileExtensionValidator

# handle file upload

class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=['html'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
