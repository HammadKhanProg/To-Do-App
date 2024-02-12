from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import taskform

def Home (request):
    tasks=Task.objects.all()

    form=taskform()
    if request.method=="POST":
        form=taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    data={
        "tasks":tasks,
        "form":form
    }
    return render(request,"home.html",data)

def Updatetask (request,pk):
    task=Task.objects.get(id=pk)
    form=taskform(instance=task)
    if request.method=="POST":
        form=taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect("home")
    data={
        "form":form
    }
    return render(request,"update.html",data)

def deletetask (request,pk):
    item=Task.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect("home")
    data={
        "item":item
    }
    return render(request,"delete.html",data)
# Create your views here.
