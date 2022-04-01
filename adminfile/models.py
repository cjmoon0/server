from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

# Create your models here.

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT,name))
        return name

class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="result/",storage=OverwriteStorage)
    dateTimeOfUpload = models.DateTimeField(auto_now=True)