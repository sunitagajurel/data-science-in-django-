"""dj_pd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from wsgiref.util import setup_testing_defaults
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view,login_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home_view,name= 'home'),
    path("login/",login_view,name= 'login_view'),
    path('performance/',include('products.urls',namespace = 'products')),
    path('upload/',include('csvs.urls',namespace = 'csvs')),
    path('customers/',include('customers.urls',namespace= 'customers'))
]

urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
