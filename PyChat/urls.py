"""PyChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
    username:saidi  pswd:mohammedsaidi157
    username:Juma Juma  pswd:Juma@1123 
    username:john-doe  pswd:johndoe123
    username:Eddie    pswd:eddiegwahisa
    username:admin     pswd:admin123
    username:habibu kyombo     pswd:habibu123 
    aggie-deo   pswd:agiedeo
"""
from django.contrib import admin
from django.urls import path, include
from registration import views as rv

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("chat.urls")),
    path('signup/', rv.SignUp, name="register"),
    path('logout/', rv.logoutUser, name="logout"),
    path("", include("django.contrib.auth.urls")),
]
