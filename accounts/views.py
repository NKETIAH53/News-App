from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            message = {
                'error':'Invalid login credentials.'
            }
            return render(request, 'accounts/login.html', message) 
        login(request, user)
        return redirect('daily_news:home')
    return render(request, 'accounts/login.html', {} )


def logout_view(request):
    if request.method == 'POST':
       logout(request)
       return redirect('main-home')
    return render(request, 'accounts/logout.html', {} )


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_object = form.save
        return redirect('accounts:login')
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)
