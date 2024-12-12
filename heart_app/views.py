from django.shortcuts import render
from .models import Doctor
# Create your views here.


# Home page
def homepage(request):
    doctors = Doctor.objects.all()[:5]
    context = {'doctors': doctors}
    return render(request, "index.html", context)


# about us part
def aboutus(request):
    return render(request, "about.html")


# blog posts
def blogpost(request):
    return render(request, 'blog.html')


# blog post details
def blogdetails(request):
    return render(request, 'blog-details.html')


# doctors list
def doctorslist(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctors.html', context)


# contactus part
def contactus(request):
    return render(request, 'contact.html')
