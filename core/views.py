from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def loginPage(request):
    page = 'login'
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('Username').lower()
        password = request.POST.get('Password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'core/login_register.html', context)

def loginUser(request):
    return render(request,'core/logged_in.html',{})