from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from bool.models import Post, Profile, Comments
# from django.core.paginator import Paginator
import random

from django.contrib.auth.models import User


class AddUser(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        nickname = request.POST['login']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=nickname, email=email)
        user.set_password(password)
        user.save()
        profile = Profile.objects.create(user=user)
        profile.save()
        return redirect('/boolseye/login')


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        nickname = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=nickname, password=password)
        if user is not None:
            login(request, user)
            return redirect('/boolseye')
        else:
            error_message = "Błędny login lub hasło."
            return render(request, 'login.html', {'error_message': error_message})


class Support(View):

    def get(self, request):
        return render(request, 'support.html')


class Account(View):
    @method_decorator(login_required)
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=user_id)
        return render(request, 'account.html', {'user': user})


class Main(View):
    def get(self, request):
        post = Post.objects.all()
        context = {"posts": post}
        return render(request, 'main.html', context)

    @method_decorator(login_required)
    def post(self, request):
        post_id = request.POST.get('post_id')
        comment_id = request.POST.get('comment_id')
        if post_id:
            post = Post.objects.get(id=post_id)
            profile = Profile.objects.get(user=request.user)
            if profile not in post.likes.all():
                post.likes.add(profile)
                post.save()
        elif comment_id:
            text = request.POST.get('text')
            comm_post = Post.objects.get(id=comment_id)
            profile = Profile.objects.get(user=request.user)
            comment = Comments.objects.create(text=text, profile=profile)
            comment.post.add(comm_post)
            comment.save()
        else:
            question = request.POST.get('question')
            answer = request.POST.get('answer')
            image = request.FILES.get('image')
            profile = Profile.objects.get(user=request.user)
            new_post = Post.objects.create(question=question, answer=answer, image=image, profile=profile)
            new_post.save()
        return redirect('/boolseye')


class Quiz(View):
    def get(self, request):
        i = 1
        list = Post.objects.all()
        posts = []
        while i <= 5:
            post = random.choice(list)
            posts.append(post)
            list = list.exclude(id=post.id)
            i += 1
        context = {"posts": posts}
        return render(request, 'quiz.html', context)


class Questions(View):
    def get(self, request):
        user_id = request.session.get('_auth_user_id')
        profile = Profile.objects.get(user_id=user_id)
        posts = Post.objects.filter(profile_id=profile)
        context = {"posts": posts}
        return render(request, 'questions.html', context)
