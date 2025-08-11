from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'books/index.html')


def show(request):
    # بيانات وهمية للكتب
    books = [
        {'id': 1, 'title': 'دليل Python', 'author': 'أحمد محمد', 'year': 2022},
        {'id': 2, 'title': 'مقدمة في Django', 'author': 'فاطمة خالد', 'year': 2023},
    ]
    return render(request, 'books/show.html', {'books': books})


def edit(request, id):
    return render(request, 'books/edit.html', {'id': id})


def delete(request, id):
    return render(request, 'books/delete.html', {'id': id})
