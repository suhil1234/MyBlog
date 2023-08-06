
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    title= models.CharField(max_length=50)
    content= models.TextField()
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    date_posted= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def commentsCount(self):
        return self.comments_set.count()

    class Meta:
        ordering =['-date_posted']
    

class Comments(models.Model):
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.content