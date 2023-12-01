from django.db import models

class Poll(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    age = models.IntegerField()
    height = models.FloatField()
    sex = models.CharField(max_length=6, choices=GENDER_CHOICES)
    favorite_color = models.CharField(max_length=20)

    def __str__(self):
        return f"Poll #{self.id}"