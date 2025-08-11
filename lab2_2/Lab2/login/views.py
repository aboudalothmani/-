from django.shortcuts import render

# Create your views here.


def loginlist(request):
    # posts = Post.objects.all().order_by('-created_at')
    return render(request, 'login.html')

# login/views.py
