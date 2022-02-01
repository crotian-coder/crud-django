from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    body = models.TextField()
    category = models.ManyToManyField(Category)
   
class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post,on_delete = models.CASCADE)



