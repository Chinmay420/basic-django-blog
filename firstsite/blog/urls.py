from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Posts

urlpatterns= [
    url(r'^$', ListView.as_view(queryset = Posts.objects.all().order_by("-date")[:25],
        template_name="blog/blogs.html")),
    url(r'^(?P<pk>\d+)$' , DetailView.as_view(model=Posts, template_name ="blog/post.html"))]
