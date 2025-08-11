from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'tasks/index.html')


def show(request):
    tasks = [
        {'id': 1, 'title': 'إنهاء الواجب'},
        {'id': 2, 'title': 'شراء البقالة'},
    ]
    return render(request, 'tasks/show.html', {'tasks': tasks})


def edit(request, id):
    return render(request, 'tasks/edit.html', {'id': id})


def delete(request, id):
    return render(request, 'tasks/delete.html', {'id': id})
