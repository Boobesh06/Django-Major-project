from django.db import models
#DataFlair Models
class majorApp(models.Model):
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    Age = models.IntegerField()
    Location = models.TextField()

    def __str__(self):
        return self.name