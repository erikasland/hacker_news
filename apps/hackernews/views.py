from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import Login, Registration, Search
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from apps.hackernews.models import Post, Comment, PostVote, CommentVote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

class Index(View):
    def get(self, request):
        infototemplate = self.InfoToTemplate()
        post = self.paginatepost(request)
        return render(request, 'hackernews/home.html', {'info': infototemplate, 'post': post})
   
    def post(self, request):
        infototemplate = self.InfoToTemplate()
        post = self.paginatepost(request)
        return render(request, 'hackernews/home.html', {'info': infototemplate, 'post': post})

    def paginatepost(self, request):
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 30)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return {'posts': posts}

    def InfoToTemplate(self):
        search = Search()
        comment = Comment.objects.all()
        postvote = PostVote.objects.all()
        commentvote = CommentVote.objects.all()

        return {'search': search, 'comment': comment, 'postvote': postvote, 'commentvote': commentvote}

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

class VoteUpPost(View):
    def post(self, request):
        post = Post.objects.filter(id = int(request.body))[0]
        user = User.objects.filter(id = request.user.id)[0]

        if not PostVote.objects.filter(post = post):
            PostVote.objects.create(post=post, vote = 1)
        else:
            postvote = PostVote.objects.filter(post = post)[0]
            postvote.vote += 1
            postvote.save()
        return JsonResponse({'status': True})

class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class CommentOnPost(View):
    def get(self, request, postid):
        infototemplate = Index.InfoToTemplate(self)
        post = Post.objects.filter(id = postid)
        postcomments = Comment.objects.all()
        print(postcomments)
        return render(request, 'hackernews/commentonpost.html', {'info': infototemplate, 'postid': postid, 'post': post, 'postcomments': postcomments})

class AddComment(View):
    def post(self, request,postid):
        comment = request.POST['comment']
        post = Post.objects.filter(id = postid)[0]
        Comment.objects.create(content = comment, post = post, user = request.user)
        return redirect('/commentonpost/' + postid)
        