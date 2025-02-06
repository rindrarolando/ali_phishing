from django.db import models

# Create your models here.

class Credentials(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    commit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username