from django.db import models
from course.models import Teacher
from django.contrib.auth.models import User

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    post = models.TextField()
    image = models.ImageField(upload_to='blog/blog')
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, null=True,blank=True)

    def __str__(self):
        return self.title