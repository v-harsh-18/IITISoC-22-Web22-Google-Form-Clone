from django.shortcuts import render
from django.contrib.auth.models import User, auth
# Create your views here.


def login(request):
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(first_name=first_name, username=username,  password=password)
        user.save()
        print('hence fucked')
        return render(request, "login.html")

    else:
        return render(request, "register.html")

