from email import message
from django.shortcuts import redirect, render
from home.models import NewPost
from django.contrib import messages
from django.db.models import Max

import datetime
from django.core.paginator import Paginator, EmptyPage
import re

# for contact:
import pymongo

from django.conf import settings
connect_string = "mongodb+srv://tejassri:Tejas2002@contactcluster.hrscy.mongodb.net/test"
my_client = pymongo.MongoClient(connect_string)

# define the database 
dbname = my_client['contact']
collection_name = dbname["contactMe"]






# Create your views here.


# Contact:
 
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check(email):
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return True
 
    else:
       return False

def contact(request):
   
   if request.method == 'POST':
      name = request.POST['name']
      email = request.POST['email']
      message = request.POST['message']
      
      if(len(name) == 0 or len(message) == 0 or check(email) == 0):
         messages.success(request, 'Please enter valid details.')
         context = {
            'name': name,
            'message': name,
            'email': email
         }
         return render(request, 'contact.html', context)
         
      
      context = {
         "name": name,
         "email": email,
         "message": message
      }
      print(context)
      # dbname.collection_name.insert(context)
      collection_name.insert(context)
      print(context)
      print("Saved to mongoDb.......................")
      
      messages.success(request, 'Message sent succesfully!!')
      return redirect('contact')
   return render(request, 'contact.html')


# All Posts:
def home(request):
   allPosts = NewPost.objects.all().order_by('-postId')
   
   # for obj in allPosts:
   #    print("Post Id = ", obj.postId)
   #    print("Topic = ", obj.topic)
   #    print("Content = ", obj.content)
   #    print(".....................")
  
   p = Paginator(allPosts, 4)
   pageNum = request.GET.get('page', 1)
   
  
   try:
      page = p.page(pageNum) 
   except EmptyPage:
      page = p.page(1) 
      
  
   context = {
      'allPosts' : page
   }
   
   return render(request, "index.html", context)


# deletes a specific post:
def confirmDelete(request ,id):
   
   thisPostDict = NewPost.objects.filter(postId=id)
   
   for thisPost in thisPostDict:
      # print("Post Id = ", thisPost.postId)
      # print("Topic = ", thisPost.topic)
      # print("Content = ", thisPost.content)
      # print(".....................")
      messages.error(request, f'Do you want to delete this post: {thisPost.topic} ?')
      context = {
         'thisPost' : thisPost
      }
  
      return render(request, "generic.html", context)

def deletePost(request, id):
   
   post = NewPost.objects.filter(postId=id)
   post.delete()
   
   messages.error(request, 'Post Deleted')
   return redirect('index')


# Update Post:
def updatePost(request, id):
   thisPostDict = NewPost.objects.filter(postId=id)
   
   for thisPost in thisPostDict:
      context = {
         'thisPost' : thisPost
      }
      
      return render(request, "updatePost.html", context)
   
# updates finally:
def updatePostHelp(request, id):
   
   thisPostDict = NewPost.objects.filter(postId=id)
   
   for thisPost in thisPostDict:
      
      if request.method == 'POST':
         print("Update ENTERED......................")
      
         topic = request.POST['topic']
         content = request.POST['content']
         
         if len(request.FILES) != 0:
            image = request.FILES['upload']
            thisPost.postImg = image
       
         
         if (not(topic and topic.strip() and content and content.strip())):
            messages.error(request, 'Topic or Content cannot be empty')
            
            # old:
            context = {
               'thisPost' : thisPost
            }
          
            return render(request, "updatePost.html", context)
        
         # update:
         
         postTime = datetime.datetime.now().strftime("%I:%M%p")
         postDate = datetime.datetime.now().strftime("%B %d, %Y")
         

         thisPost.postDate = postDate
         thisPost.postTime = postTime
         thisPost.topic = topic.lower()
         thisPost.content = content
         thisPost.postId = id
         
         thisPost.save()
                
         
         # messages.success(request, 'Post updated successfully!!', extra_tags='update')
         
         print("Post Id = ", id)
         print("Topic = ", topic)
         print("Content = ", content)
         print("UPDATED.....................")
         
         context = {
            'thisPost' : thisPost
         }
         return render(request, "generic.html", context)
         

# search posts:
def searchPage(request):
   if request.method == 'POST':
           
      data = request.POST['data']
      print("Say yes -> ", data)
      
      # if data not valid:
      if len(data) == 0:
         messages.success(request, "Error: Enter valid search details.")
         return render(request, "searchPage.html")
      
      dt = data.split()
      #  day month year
      
      # if date:
      if dt[0].isdecimal() and dt[1].isdecimal() and dt[2].isdecimal():
         print("IT IS A DATE....................")
         
         dt = list(map(int, dt))
         print(dt)
         
         day, month, year = dt[0], dt[1], dt[2]
         
         if (month < 1 or month > 12) or (day < 1 or day > 31) or (year < 1):
            messages.success(request, "Error: Enter valid search details.")
            return render(request, "searchPage.html")
         
         x = datetime.datetime(year, month, day)
         postDate = (x.strftime("%b %d, %Y"))
         
         print(dt)
         print(postDate)
         
         allPosts = NewPost.objects.filter(postDate=postDate)
         
         if len(allPosts) == 0:
            print("0 results")
            messages.success(request, 'No results found.')
            return render(request, "searchPage.html")
         
         messages.success(request, f'{len(allPosts)} search results found.')
         
         # p = Paginator(allPosts, 4)
         # pageNum = request.GET.get('page', 1)
         
      
         # try:
         #    page = p.page(pageNum) 
         # except EmptyPage:
         #    page = p.page(1) 
            
      
         # context = {
         #    'allPosts' : page
         # }
         context = {
            'allPosts' : allPosts
         }
         
         return render(request, "searchPage.html", context)
      
      # if topic:
      else:
         print("IT IS A TOPIC_______________________")
         print(data)
         allPosts = NewPost.objects.filter(topic__contains=data)

         for obj in allPosts:
            print("Post Id = ", obj.postId)
            print("Topic = ", obj.topic)
            print("Content = ", obj.content)
            print("Img = ", obj.postImg)
            print(".....................")
         
         # if no results:
         if len(allPosts) == 0:
            print("0 results")
            messages.success(request, 'No results found.')
            return render(request, "searchPage.html")
         
         messages.success(request, f'{len(allPosts)} search results found.')
         # p = Paginator(allPosts, 4)
         # pageNum = request.GET.get('page', 1)
         
      
         # try:
         #    page = p.page(pageNum) 
         # except EmptyPage:
         #    page = p.page(1) 
            
      
         # context = {
         #    'allPosts' : page
         # }
         context = {
            'allPosts' : allPosts
         }
         
         return render(request, "searchPage.html", context)
              
      
   else:
      print("NOTHING>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
      return render(request, "searchPage.html")

# About Specific Post:
def generic(request, id):
   thisPostDict = NewPost.objects.filter(postId=id)
   
   for thisPost in thisPostDict:
      # print("Post Id = ", thisPost.postId)
      # print("Topic = ", thisPost.topic)
      # print("Content = ", thisPost.content)
      # print(".....................")
      
      context = {
         'thisPost' : thisPost
      }
      print(context)
      return render(request, "generic.html", context)


# Add Post:
def elements(request):
   
   if request.method == 'POST':
      print("ENTERED......................")
      
      topic = request.POST['topic']
      content = request.POST['content']
           
      if (not(topic and topic.strip() and content and content.strip())):
         messages.error(request, 'Topic or Content cannot be empty')
         return render(request, 'elements.html')
      
      dict = NewPost.objects.aggregate(Max('postId'))
      
      if NewPost.objects.all().count() == 0:
         postId = 1
      else:
         postId = dict['postId__max'] + 1

      postTime = datetime.datetime.now().strftime("%I:%M%p")
      postDate = datetime.datetime.now().strftime("%B %d, %Y")
      
      
      if len(request.FILES) != 0:
         image = request.FILES['upload']
         newPost = NewPost(postTime=postTime, postDate=postDate, topic=topic.lower(), content=content, postId=postId, postImg=image) 
         newPost.save()
      else:
         newPost = NewPost(postTime=postTime, postDate=postDate, topic=topic.lower(), content=content, postId=postId) 
         newPost.save()
      
      messages.success(request, 'Post added successfully!!')
      
      print("Post Id = ", postId)
      print("Topic = ", topic)
      print("Content = ", content)
      # print("Img = ", image)
      print("SAVED.....................")
        
      return redirect('elements')
   
   return render(request, "elements.html")