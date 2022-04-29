from django.db import models
from django.contrib.auth.models import User


# class Creators(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     othername = models.CharField(label='othername', max_length=120)
#     username = models.CharField(label='username', max_length=120, unique=True, required=True)
#     date_of_birth = models.DateTimeField(label = 'date_of_birth',  )

#     def __str__(self):
#         return self.user
        