from django.shortcuts import render
# 导入HttpResponse
from django.http import HttpResponse


# Create your views here.

# 定义试图函数
from book.models import BookInfo


def index(request):
    context = {
        'name': '阿三'
    }

    return render(request, 'index.html', context=context)

    return HttpResponse('OK!')

def booklist(request):

    books = BookInfo.objects.all()

    context = {
        'books':books
    }

    return render(request,'booklist.html',context=context)

    return HttpResponse('booklist')