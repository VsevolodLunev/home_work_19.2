from django.shortcuts import render


def home(request):
    return render(request, 'project_sky/home.html')


def contacts(request):
    return render(request, 'contacts.html')
