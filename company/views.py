from django.shortcuts import render, redirect

from company.models import Company
# from django.contrib.auth.models import User


# Create your views here.

# Company Views


def register(request):
    if request.method == 'POST':
        companyName = request.POST.get('cname')
        companyLogo = request.POST.get('clogo')
        companySize = request.POST.get('csize')

        current_user = request.user

        registration = Company(
            company_name=companyName, company_logo=companyLogo, company_size=companySize, company_created_by=current_user)
        registration.save()
        return redirect('home')

    return render(request, 'companyRegister.html')


def update(request):

    pass
