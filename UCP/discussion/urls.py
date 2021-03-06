"""
Urls file for Discussion App

contains url patterns for the frontend pages of the discussion app
"""

from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView

from discussion import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/unsubscribe', views.UnSubscribe.as_view(), name='reply'),
    url(r'^(?P<pk>[0-9]+)/subscribe', views.Subscribe.as_view(), name='reply'),
    url(r'^(?P<pk>[0-9]+)/reply', views.Reply.as_view(), name='reply'),
    url(r'^(?P<pk>[0-9]+)', views.DiscussionDetails.as_view(), name='discussion_detail'),
    url(r'^add', views.AddDiscussion.as_view(), name='add-discussion'),
    url(r'^', views.DiscussionList.as_view(), name='discussion_list'),
]
