from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=126)
    tokens = models.IntegerField(default=4000)
    auth_token = models.CharField(max_length=128,blank=True,null=True)
    
    def _str__(self):
        return self.username
    
    
class Chat(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}-{self.timestamp}"
    
    