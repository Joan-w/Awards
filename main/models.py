from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    # fields for the project table
    name = models.CharField(max_length=300)
    image = models.ImageField(blank=True, null=True)
    reviewDate = models.DateTimeField(default=timezone.now())
    languages = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    projectLink = models.CharField(max_length=300)
    averageRating = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Review(models.Model):
    # fields for the review table
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username