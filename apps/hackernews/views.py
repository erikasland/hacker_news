from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import Login, Registration, Search
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

class Index(View):
    def get(self, request):
        search = Search()
        return render(request, 'hackernews/home.html', {'search': search})
    def post(self, request):
        search = Search()
        return render(request, 'hackernews/home.html', {'search': search})

class LogReg(View):
    def get(self, request):
        Log = Login()
        Reg = Registration()
        return render(request, 'hackernews/index.html', {'login': Log, 'register': Reg})

class LoginUser(View):
    def post(self, request):
        form = Login(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        return redirect('/logreg')

class RegUser(View):
    def post(self, request):
        form = Registration(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            if form['password'] != form['confirm']:
                return redirect('/logreg')
            else:
                User.objects.create_user(username = form['username'], email = form['email'], password = form['password'])
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                login(request, user)
                return redirect('/')

class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('/')