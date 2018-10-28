from django.conf.urls import url
from book.views import index,booklist

urlpatterns = [
    url(r'^index/$',index),
    url(r'^booklist/$',booklist),
]