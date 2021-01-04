from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
