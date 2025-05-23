from django.db import models
from django.urls import reverse

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("tasks:tasks-detail", kwargs={"id": self.id})