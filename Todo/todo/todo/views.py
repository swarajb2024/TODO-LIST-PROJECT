from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from todo.models import TODOO
from django.db import IntegrityError
from django.contrib import messages


def signup(request):
    if request.method == "POST":
        username = request.POST.get('fnm')
        email = request.POST.get('email')
        password = request.POST.get('pwd')

        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect('login')

        except IntegrityError:
            messages.error(request, "Username already exists")

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('fnm')
        pwd = request.POST.get('pwd')

        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('todopage')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


def todo(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            TODOO.objects.create(title=title, user=request.user)
        return redirect('todopage')

    rest = TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'rest': rest})


def edit_todo(request, srno):
    if not request.user.is_authenticated:
        return redirect('login')

    # ✅ FIX HERE
    todo = TODOO.objects.get(sr_no=srno, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            todo.title = title
            todo.save()
            return redirect('todopage')

    return render(request, 'edit_todo.html', {'todo': todo})


def delete_todo(request, srno):
    if not request.user.is_authenticated:
        return redirect('login')

    # ✅ FIX HERE
    todo = TODOO.objects.get(sr_no=srno, user=request.user)
    todo.delete()
    return redirect('todopage')


def signout(request):
    logout(request)
    return redirect('login')