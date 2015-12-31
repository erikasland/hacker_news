from django.conf.urls import url
from apps.hackernews.views import Index, LoginUser, RegUser, LogReg, LogOut, VoteUpPost

urlpatterns = [
    url(r'^reg$', RegUser.as_view()),
    url(r'^login$', LoginUser.as_view()),
    url(r'^logreg$', LogReg.as_view()),
    url(r'^logout$', LogOut.as_view()),
    url(r'^voteuppost$', VoteUpPost.as_view()),
    url(r'^', Index.as_view()),
]