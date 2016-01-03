from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=255)
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.post.title

class PostVote(models.Model):
    vote = models.IntegerField(default=0)
    post = models.ForeignKey(Post, related_name='post_vote')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.post.title

class CommentVote(models.Model):
    vote = models.IntegerField(default=0)
    comment = models.ForeignKey(Comment, related_name='comment_vote')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment.post.title