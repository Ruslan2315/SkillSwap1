from django.contrib import messages
from .models import News, Category, Comment
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import SignUpForm
from django.urls import reverse_lazy


def home(request):
    first_news = News.objects.first()
    three_news = News.objects.all()[1:3]
    three_categories = Category.objects.all()[0:3]
    return render(request,'home.html',{
        'first_news':first_news,
        'three_news':three_news,
        'three_categories':three_categories
    })


def all_news(request):
    all_news=News.objects.all()
    return render(request,'all-news.html',{
        'all_news':all_news
    })


def detail(request,id):
    news=News.objects.get(pk=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        comment=request.POST['message']
        Comment.objects.create(
            news=news,
            name=name,
            email=email,
            comment=comment
        )
        messages.success(request,'Comment submitted but in moderation mode.')
    category = Category.objects.get(id=news.category.id)
    rel_news = News.objects.filter(category=category).exclude(id=id)
    comments = Comment.objects.filter(news=news, status=True).order_by('-id')
    return render(request, 'detail.html',{
        'news': news,
        'related_news': rel_news,
        'comments': comments
    })


def all_category(request):
    cats = Category.objects.all()
    return render(request,'category.html',{
        'cats':cats
    })


def category(request,id):
    category = Category.objects.get(id=id)
    news = News.objects.filter(category=category)
    return render(request,'category-news.html',{
        'all_news':news,
        'category':category
    })


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




# @login_required
# def add_comment(request):
#     if request.method == 'POST':
#     return render(request, 'detail.html')

