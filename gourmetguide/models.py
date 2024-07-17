from django.db import models
# Import the User
# from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()

  # override __str__ method to return the diary title attribute
    def __str__(self):
        return self.title
    
    # # Add the foreign key linking to a user instance
    # user = models.ForeignKey(User, on_delete=models.CASCADE)