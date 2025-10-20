from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import AuthorForm, CategoryForm, PostForm, PostSearchForm
from .models import Post, Author
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            author, _ = Author.objects.get_or_create(
                name=request.user.username,
                defaults={'email': f'{request.user.username}@example.com'}
            )
            post.author = author
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/form_post.html', {'form': form})

def post_search(request):
    form = PostSearchForm(request.GET or None)
    results = []
    if form.is_valid():
        q = form.cleaned_data['q']
        if q:
            results = Post.objects.filter(
                Q(title__icontains=q) | Q(content__icontains=q)
            ).select_related('author', 'category').order_by('-created_at')
    return render(request, 'blog/search.html', {'form': form, 'results': results})

def home(request):
    posts = Post.objects.select_related('author', 'category').order_by('-created_at')[:10]
    return render(request, 'blog/home.html', {'posts': posts})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'blog/form_author.html', {'form': form})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'blog/form_category.html', {'form': form})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/form_post.html', {'form': form})

def post_search(request):
    form = PostSearchForm(request.GET or None)
    results = []
    if form.is_valid():
        q = form.cleaned_data['q']
        if q:
            results = Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))\
                                  .select_related('author', 'category').order_by('-created_at')
    return render(request, 'blog/search.html', {'form': form, 'results': results})
