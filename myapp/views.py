from django.shortcuts import render, redirect

from myapp.forms import todoform
from myapp.models import Todo


# Create your views here.
def todo(request):
    return render(request,"todo.html")


def dash(request):
    return render(request,"dash.html",)

def form(request):
    if request.method == 'POST':
        obj = todoform(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect("/")
    data = todoform()
    return render(request,"form.html",{'todoform':data})


def data(request):
    data=Todo.objects.all()    #returns a list of all model objects
    print(data)
    return render(request, "data.html",{'data':data})


def delete_1(request,obj_id):
    data = Todo.objects.get(id=obj_id)
    print(data)
    data.delete()
    return redirect('data')

def update_1(request,obj_id):
    obj=Todo.objects.get(id=obj_id)
    form=todoform(instance=obj)
    if request.method =='POST':
        form=todoform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("data")
    return render(request,"update.html",{'form':form})
