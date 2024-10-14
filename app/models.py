from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=250)
    description=models.CharField(max_length=250,null=True,blank=True)  
    body=models.TextField()  
    image=models.ImageField(upload_to="blog")
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    """ subscribe=models.BooleanField ()  """
    """ rating=models.IntegerField ()"""
    """ null and blank means it can be optional """
    created_at=models.DateTimeField(auto_now_add=True)
    """ when you add date to it that is auto_now_add"""
    updated_at=models.DateTimeField(auto_now=True)
    """ when you add something new to an existing stuff is auto_now """
    def __str__(self):
        return f"{self.title} created on {self.created_at}"
class Comment(models.Model):
    owner= models.ForeignKey(User,on_delete=models.CASCADE)
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE)
    body=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.owner.username}'s comment on {self.blog.title} on {self.created_at}"


