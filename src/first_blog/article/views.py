from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post
from datetime import datetime
from .forms import ArticleForm, ArticleModelForm


# Create your views here.
def index(request):
    context = {
        'django': True,
        'flask': True,
        'pehape': False,
        'now': datetime.now()
    }
    return render(request, 'templates/article/index.html', context)


# fails because only the first object is gets
def individual_post(response):
    recent_post = Post.objects.all()
    # recent_post = Post.objects.get(id__exact=1)
    for i in recent_post:
        return HttpResponse(i.title + ': ' + i.content)


def post_list(request):
    queryset = Post.objects.all()
    return render(request, 'templates/article/post_list.html', {'postlar': queryset})


def something_new(request):
    new_stuff = """<h1>Is this a header?<h1/>"""
    return HttpResponse(new_stuff)


def create_post(request):
    form = ArticleForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            header = form.cleaned_data['header']
            content = form.cleaned_data['content']
            liked = form.cleaned_data['liked']
            draft = form.cleaned_data['draft']
            post = Post.objects.create(
                header=header, content=content, liked=liked, draft=draft, owner=request.user
            )
            post.save()
            queryset = Post.objects.all()

            return render(request, 'templates/article/post_list.html', {'postlar': queryset})
        else:
            return HttpResponse("aaa")
    else:
        return render(request, 'templates/article/post_create.html', {'form': form})


def create_post_mf(request):
    form = ArticleModelForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = request.user

            form.save()
            queryset = Post.objects.all()

            return render(request, 'templates/article/post_list.html', {'postlar': queryset})
        else:
            return HttpResponse("aaa")
    else:
        return render(request, 'templates/article/post_create.html', {'form': form})


def post_detail(request, post_id):
    # try:
    #     pk = Post.objects.get(id__exact=post_id)
    # except Post.DoesNotExist:
    #     raise Http404('noooooooooooooooo')
    # pk = Post.objects.get(id__exact=post_id)
    post = get_object_or_404(Post, id__exact=post_id)
    comments = post.comments.all()
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'templates/article/individual_post.html', context)
