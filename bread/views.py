from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Details
from django.contrib.auth.models import User, auth
from company.models import *


def login(request):
    if request.method == "POST":
        username = request.POST.get('userName')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            # print("Login Success")
            messages.add_message(request, messages.INFO, "Login Successfull")
            return render(request, 'home.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def update(request):
    currentuser = request.user
    c = User.objects.filter(username=currentuser)
    print(c.values)
    return render(request, 'updateUser.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        print(first_name)
        last_name = request.POST.get('lastName')
        username = request.POST.get('userName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User is not None:
            pass

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.INFO, "Username Taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.add_message(request, messages.INFO, "Email Exist")
                return redirect("register")

            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email,  first_name=first_name, last_name=last_name)
                user.save()

            print("userCreated")
            messages.add_message(request, messages.INFO, 'User Created')
            return redirect('login')

    else:
        return render(request, 'register.html')


def home(request):
    current_user = request.user
    if Company.objects.filter(company_created_by=current_user).exists():
        companies = Company.objects.filter(company_created_by=current_user)
        val = companies.values()
        print(val)
        title = "HomePage"
        return render(request, 'home.html', {'company': val})
    else:
        return render(request, 'home.html')

    # return render(request, 'home.html', {'data': det})


def add(request):
    val1 = int(request.POST['val1'])
    val2 = int(request.POST['val2'])
    res = val1+val2
    title = "Result"
    return render(request, 'result.html', {'result': res, 'title': title})
