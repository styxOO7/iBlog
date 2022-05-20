from django.db import models

import datetime

from django.conf import settings

# Create your models here.
class NewPost(models.Model):
    
    # today = date.today()
    # d = today.strftime("%B %d, %Y")
    # postTime = datetime.datetime.now().strftime("%I:%M%p")
    # postDate = datetime.datetime.now().strftime("%B %d, %Y")
    
    
    topic = models.CharField(max_length=30)
    content = models.TextField()
    postId = models.IntegerField()
    
    postTime = models.TextField(default=datetime.datetime.now().strftime("%I:%M%p"))
    postDate = models.TextField(default=datetime.datetime.now().strftime("%B %d, %Y"))
    
    postImg = models.ImageField(upload_to = "images", null=True, blank=True, default='pic02.jpg')
    
    print("WORKING.................")
    
    # for name save:
    def __str__(self):
        return str(self.postId) + str(" ") + self.topic
    
    
    
    


