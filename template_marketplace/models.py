from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.core.files.storage import FileSystemStorage
import os

class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=['zip'])])
    description = models.TextField(default='No description provided.')
    image_banner = models.ImageField(upload_to='banners/', default = 'default.jpg')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def file_url(self):
        if self.file.name.endswith('.zip'):
            return os.path.join(settings.MEDIA_URL, f'extracted/{self.id}/index.html')
        return None