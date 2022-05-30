from django.db import models

# Create your models here.


class jsonData(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    userId = models.IntegerField(null=True)
    title = models.TextField(null=True)
    body = models.TextField(null=True)

    # def __str__(self):
    #     return self.userId
