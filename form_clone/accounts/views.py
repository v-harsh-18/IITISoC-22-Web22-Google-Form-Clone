from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, "index.html")
        else:
            messages.info(request,"Nigga! couldn't recognize yo' ass")
            return redirect("login")
    else:
        return render(request, "login.html")            

   

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"email already exists")
            else:
                user = User.objects.create_user(first_name=first_name, username=username,  password=password)
                user.save()
                
                return render(request, "login.html")
        else:
            messages.info(request,"passwords shi se likh le lodu")
        return render(request, "register.html")
    else:
        return render(request, "register.html")

