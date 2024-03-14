from django.shortcuts import render, redirect

from myapp.forms import todoform


# Create your views here.
def test1(request):
    return render(request,"todo.html")


def test2(request):
    if request.method=='POST':
        obj=todoform(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("/")
    data = todoform()
    return render(request,"dash.html",{'todoform':data})

def test3(request):
    if request.method == 'POST':
        obj = todoform(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("/")
    data = todoform()
    return render(request,"form.html",{'todoform':data})

def test4(request):
    return render(request,"new.html")