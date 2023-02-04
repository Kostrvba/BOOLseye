from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View

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
            user_id = request.POST['login']
            response = render(request, 'logged.html')
            response.set_cookie('user_id', user_id)
            return response
        else:
            error_message = "Błędny login lub hasło."
            return render(request, 'login.html', {'error_message': error_message})

class Support(View):

    def get(self, request):
        return render(request, 'support.html')


