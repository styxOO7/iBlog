from django.db import models
from datetime import date





# Create your models here.
class NewPost(models.Model):
    
    today = date.today()
    d = today.strftime("%B %d, %Y")
    
    postDate = d
    topic = models.CharField(max_length=30)
    content = models.TextField()
    postId = models.IntegerField()
    
    print("WORKING.................")
    
    # for name save:
    def __str__(self):
        return str(self.postId) + str(" ") + self.topic
    
    
    
    


