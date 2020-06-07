from django.db import models

# Create your models here.
class Project(models.Model):
    # fields for the project table
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/', null=True)
    reviewDate = models.DateField()
    languages = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    projectLink = models.CharField(max_length=300)
    averageRating = models.FloatField()

    def __str__(self):
        return self.name