from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.aboutus, name='about'),
    path('blog/', views.blogpost, name='blog'),
    path('blog/blog-detail/', views.blogdetails, name='blogdetail'),
    path('doctors/', views.doctorslist, name='doctors'),
    path('contact/', views.contactus, name='contact')
]
