from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    publish_date = models.DateTimeField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # upvotes = models.ManyToManyField(User,)
    # downvotes
    # likes = models.ManyToManyField(User,)
    
    def get_absolute_url(self):
        return reverse("daily_news:detail", kwargs={"id": self.id})
    
    def __str__(self):
        return self.title
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    othername = models.CharField(max_length=120)
    username = models.CharField( max_length=120, unique=True, null=False)
    bio = models.TextField()
    date_of_birth = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return str(self.user)
        