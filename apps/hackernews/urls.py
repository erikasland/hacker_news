from django.conf.urls import url
from apps.hackernews.views import Index, LoginUser, RegUser, LogReg, LogOut, VoteUpPost, CommentOnPost, AddComment, Submit, SubmitPost

urlpatterns = [
    url(r'^reg$', RegUser.as_view()),
    url(r'^login$', LoginUser.as_view()),
    url(r'^logreg$', LogReg.as_view()),
    url(r'^logout$', LogOut.as_view()),
    url(r'^submit$', Submit.as_view()),
    url(r'^submitpost$', SubmitPost.as_view()),
    url(r'^voteuppost$', VoteUpPost.as_view()),
    url(r'^addcomment/(?P<postid>\d+)$', AddComment.as_view()),
    url(r'^commentonpost/(?P<postid>\d+)$', CommentOnPost.as_view()),
    url(r'^', Index.as_view()),
]