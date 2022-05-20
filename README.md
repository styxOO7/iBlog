# iBlog
full stack Blog web application using Django <br>


Live: https://iblogwebsite.herokuapp.com/index <br>

Tech: <br>
HTML, CSS, JS  <br>
Django 3 <br>
MongoDb <br>

Main page -> show all posts with Posting Date and Time (under IST using pillow). <br>
Generic page -> to read more about the selected post. <br> <br>
Search page-> filter posts using topic or date entered (with constraints of valid/invalid date added). <br>
Add Post page -> user to add new post with topic, content + upload image feature (if no image selected -> a default image from database). <br>
Update Post page -> user to update topic, content and change uploaded image for selected post. <br>
CRUD: allows user to perform CRUD with fields topic/content/image with a default pic in case of empty image. <br>
save to mongo db using pymongo for contact and djongo for all post model data. <br>
 <br>
Additionally : <br>
Added pagination to the main page using Paginator module in Python. <br>
Exploited Django messages for various alerts and confirmations during add and update feature. <br>
Contact page for contacting the admin. <br>



