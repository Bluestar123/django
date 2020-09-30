"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from first import views
from first.views import onemore as views1

urlpatterns = [
    # path('admin/', admin.site.urls, name='admin'),
    # path('first', views.index, name='first'),
    # path('first/get_user', views.post, name='getuser'),
    # path('login', views.get_csrf),

    # path('add_book', views.add_book),
    # path('get_book', views.get_book),
    # path('get_book_by_id', views.get_book_by_id),


    path('add_book1', views1.add_book),
    path('add_author', views1.add_author)
]
