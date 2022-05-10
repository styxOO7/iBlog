from django.shortcuts import redirect, render
from home.models import NewPost
from django.contrib import messages
from django.db.models import Max


from django.core.paginator import Paginator, EmptyPage


# Create your views here.
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

      
      newPost = NewPost(topic=topic, content=content, postId=postId) 
      newPost.save()
      
      messages.success(request, 'Post added successfully!!')
      
      print("Post Id = ", postId)
      print("Topic = ", topic)
      print("Content = ", content)
      print("SAVED.....................")
        
      return redirect('elements')
   
   return render(request, "elements.html")