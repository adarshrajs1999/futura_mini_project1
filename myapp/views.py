from django.shortcuts import render, redirect

from myapp.forms import todoform
from myapp.models import Todo


# Create your views here.
def todo(request):
    return render(request,"todo.html")


def dash(request):
    return render(request,"dash.html",)

def create(request):
    if request.method == 'POST':
        obj = todoform(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("/")
    data = todoform()
    return render(request,"create.html",{'todoform':data})


def read(request):
    data=Todo.objects.all()    #returns a list of all model objects
    print(data)
    return render(request, "read.html",{'data':data})


def delete_1(request,id):
    data = Todo.objects.get(id=id)
    print(data)
    data.delete()
    return redirect("read")

def update_1(request,id):
    obj=Todo.objects.get(id=id)
    form=todoform(instance=obj)
    if request.method =='POST':
        form=todoform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("read")
    return render(request,"update.html",{'form':form})
