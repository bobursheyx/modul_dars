from django.shortcuts import render
from django.views import View
from .models import Blog

class BlogListView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        contex = {
            'blogs':blogs,
        }
        return render(request, 'main/blog.html', contex)