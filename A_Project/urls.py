"""
URL configuration for A_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from z_account import views
# from z_admin import views
# from z_user import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing-page'), # landing page


    # Include the app's urls.py file
    # path('account/', include('z_account.urls')),
    path('user-admin/', include('z_admin.urls')),
    path('user/', include('z_user.urls')),
]
