from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    address = models.TextField()
    preview_image = models.ImageField(upload_to='event_previews/')
    short_description = models.TextField()
    full_description = models.TextField()
    category = models.CharField(max_length=50)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Пример значения по умолчанию
    created_at = models.DateTimeField(default=timezone.now)  # Текущая дата и время по умолчанию
    # ... другие поля ...

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_datetime']


class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, default="astana")  # Новое поле для города
    image = models.ImageField(upload_to='place_images/')
    short_description = models.TextField()
    full_description = models.TextField()
    phone_number = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Пример значения по умолчанию
    created_at = models.DateTimeField(default=timezone.now)  # Текущая дата и время по умолчанию
    # ... другие поля ...

    def __str__(self):
        return self.name
    

