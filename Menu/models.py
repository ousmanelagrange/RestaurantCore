from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"