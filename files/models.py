from django.db import models


class File(models.Model):

    file = models.FileField(upload_to='uploads')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
