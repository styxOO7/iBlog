from django.db import models

import datetime
from blog import settings

# Add the import for GridFSStorage
from djongo.storage import GridFSStorage

# Define your GrifFSStorage instance 
# grid_fs_storage = GridFSStorage(collection='images')

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
    
    # postImg = models.ImageField(upload_to = "images",  storage=grid_fs_storage, null=True, blank=True, default='pic02.jpg')
    
    postImg = models.ImageField(upload_to = "images", null=True, blank=True, default='pic02.jpg')
    
    print("WORKING.................")
    
    # for name save:
    def __str__(self):
        return str(self.postId) + str(" ") + self.topic
    
    
    
    


