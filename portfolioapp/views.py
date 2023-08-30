from django.shortcuts import render,redirect
from .models import promodel

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email= request.POST.get('email')
        subject = request.POST.get('subject')
        message= request.POST.get('message')
        a = promodel.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        a.save()  
        return redirect('index')
    return render(request,'index.html')