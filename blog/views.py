from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from blog.models import Posts

# Create your views here.
@login_required
def index(request):
    posts= Posts.objects.all()
    if request.method =='POST':
       form = PostForm(request.POST)
       if form.is_valid:
           instance = form.save(commit=False)
           instance.author= request.user
           instance.save()
           return redirect("blog-index")
    else:
        form =PostForm()
    context ={
        'posts':posts,
        'form':form      }
    return render(request,'blog/index.html',context)

@login_required
def postDetail(request,pk):
    post = Posts.objects.get(id=pk)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid() :
            instance = form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect("post-detail",pk=pk)
    else :
        form = CommentForm()
    context ={'post':post,
              'form': form}
    return render(request,'blog/post-detail.html',context)    

@login_required
def postEdit(request,pk):
    post = Posts.objects.get(id=pk)
    if request.method=='POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid() :
            form.save()
            return redirect("post-detail",pk=pk)
    else :
        form = PostForm(instance=post)
    context ={'post':post,
              'form': form}
    return render(request,'blog/post-edit.html',context) 

@login_required
def postDelete(request,pk):
    post = Posts.objects.get(id=pk)
    if request.method=='POST':
        post.delete()
        return redirect("blog-index")
    context ={'post':post}
    return render(request,'blog/post-delete.html',context)
    
