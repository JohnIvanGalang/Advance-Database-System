from django.urls import path
from . import views

# app_name = 'z_user'


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('edit-profile/', views.edit_profile, name='edit-profile'),

    path('landing-page/', views.landing_page, name='landing-page'),
    path('homepage/', views.homepage, name='homepage'),
    path('profile/', views.profile, name='profile'),
    path('coffee/', views.coffee, name='coffee'),
    
    path('coffee/<int:pk>/', views.coffee, name='coffee'),

    # path('order-coffee/<int:pk>/', views.order_coffee, name='order-coffee'),
]

