from django.db import models

class Poll(models.Model):
    age = models.IntegerField()
    height = models.FloatField()
    sex = models.CharField(max_length=10)
    favorite_color = models.CharField(max_length=20)

    def __str__(self):
        return f"Poll #{self.id}"