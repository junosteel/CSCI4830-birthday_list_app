from django.db import models

# Create your models here.
class Birthday(models.Model):
    PRIORITY_CHOICES = [
        ('Acquaintance', 'Acquaintance'),
        ('Friend', 'Friend'),
        ('Family', 'Family'),
    ]

    name = models.CharField(max_length=225)
    birth_date = models.DateField()
    gifts = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Friend')

    def __str__(self):
        return f"{self.name} - {self.birth_date}"