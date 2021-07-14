from django.contrib import admin
from django.urls import path
from authentication import views
from urlhandler import views as views1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views1.home, name='home'),
    path('<str:short_url>', views1.home, name='home'),
    path('dashboard/', views1.dashboard, name='dashboard'),
    path('generater/', views1.generater, name='generater'),
    path('signup/', views.userSignup, name='signup'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
]
