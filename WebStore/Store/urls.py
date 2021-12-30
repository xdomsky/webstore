from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'Store'
urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('account/', views.account, name='account'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('<str:username>/', views.user, name='user'),
]
urlpatterns += staticfiles_urlpatterns()
