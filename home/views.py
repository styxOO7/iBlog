from email import message
from django.shortcuts import redirect, render
from home.models import NewPost
from django.contrib import messages
from django.db.models import Max

import datetime
from django.core.paginator import Paginator, EmptyPage


# Create your views here.

# All Posts:
def home(request):
   allPosts = NewPost.objects.all()
   
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
      
      # if date:
      if dt[0].isdecimal() and dt[1].isdecimal() and dt[2].isdecimal():
         print("IT IS A DATE....................")
         
         dt = list(map(int, dt))
         x = datetime.datetime(dt[0], dt[1], dt[2])
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
         allPosts = NewPost.objects.filter(topic__startswith=data)

         # for obj in allPosts:
         #    print("Post Id = ", obj.postId)
         #    print("Topic = ", obj.topic)
         #    print("Content = ", obj.content)
         #    print(".....................")
         
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
      # newPost = NewPost(request.POST)
      
      topic = request.POST['topic']
      content = request.POST['content']
      
      if (not(topic and topic.strip() and content and content.strip())):
         messages.error(request, 'Topic or Content cannot be empty')
         # return render(request, 'elements', message='Topic or Content cannot be empty')
         return render(request, 'elements.html')
      
      # postId = NewPost.objects.all().count() + 1
      dict = NewPost.objects.aggregate(Max('postId'))
      
      if NewPost.objects.all().count() == 0:
         postId = 1
      else:
         postId = dict['postId__max'] + 1

      postTime = datetime.datetime.now().strftime("%I:%M%p")
      postDate = datetime.datetime.now().strftime("%B %d, %Y")
      
      newPost = NewPost(postTime=postTime, postDate=postDate, topic=topic.lower(), content=content, postId=postId) 
      newPost.save()
      
      messages.success(request, 'Post added successfully!!')
      
      print("Post Id = ", postId)
      print("Topic = ", topic)
      print("Content = ", content)
      print("SAVED.....................")
        
      return redirect('elements')
   
   return render(request, "elements.html")