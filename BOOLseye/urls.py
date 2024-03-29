"""BOOLseye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bool import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.AddUser.as_view(), name="register"),
    path('login/', views.Login.as_view(), name="login"),
    path('support/', views.Support.as_view(), name="support"),
    path('account/', views.Account.as_view(), name="account"),
    path('', views.Main.as_view(), name="main"),
    path('quiz/', views.Quiz.as_view(), name="quiz"),
    path('account/questions/', views.Questions.as_view()),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
