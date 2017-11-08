# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag
from markdown import markdown
from django.views.generic import ListView
# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def index2(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index2.html', context={'post_list': post_list})

def portfolio(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/portfolio.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown(post.body)
    return render(request, 'blog/portfolio-page.html', context={'post': post})

    #return render(request, 'blog/index.html', context={
    #   'title': '我的博客首页',
    #   'welcome': '欢迎欢迎，热烈欢迎。'
    #})
def archives(request, year, month):
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month
    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/portfolio.html', context={'post_list': post_list})

class TagView(ListView):
    model = Post
    template_name = 'blog/portfolio.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)