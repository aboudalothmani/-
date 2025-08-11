from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'notes/index.html')


def show(request):
    # بيانات وهمية (مثل ما تم في المعمل)
    notes = [
        {'id': 1, 'title': 'ملاحظة حول المحاضرة',
            'content': 'تم شرح استخدام القوالب في Django'},
        {'id': 2, 'title': 'ملاحظة شخصية', 'content': 'لا تنسَ تسليم الواجب'},
    ]
    return render(request, 'notes/show.html', {'notes': notes})


def edit(request, id):
    # إرسال المعرف إلى القالب
    return render(request, 'notes/edit.html', {'id': id})


def delete(request, id):
    # إرسال المعرف إلى القالب
    return render(request, 'notes/delete.html', {'id': id})
