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
from django.urls import path, include
from bool import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('boolseye/register/', views.AddUser.as_view(), name="register"),
    path('boolseye/login/', views.Login.as_view(), name="login"),
    path('boolseye/support/', views.Support.as_view(), name="support"),
    path('boolseye/account/', views.Account.as_view(), name="account"),
    path('boolseye/', views.Main.as_view(), name="main"),
    path('boolseye/quiz/', views.Quiz.as_view(), name="quiz"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
