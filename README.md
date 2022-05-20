# iBlog
full stack Blog web application using Django


Live: https://iblogwebsite.herokuapp.com/index <br>

Tech:
HTML, CSS, JS
Django 3
MongoDb

Main page -> show all posts with Posting Date and Time (under IST using pillow).
Generic page -> to read more about the selected post.
Search page-> filter posts using topic or date entered (with constraints of valid/invalid date added).
Add Post page -> user to add new post with topic, content + upload image feature (if no image selected -> a default image from database).
Update Post page -> user to update topic, content and change uploaded image for selected post.
CRUD: allows user to perform CRUD with fields topic/content/image with a default pic in case of empty image.
save to mongo db using pymongo for contact and djongo for all post model data.

Additionally :
Added pagination to the main page using Paginator module in Python.
Exploited Django messages for various alerts and confirmations during add and update feature.
Contact page for contacting the admin.



