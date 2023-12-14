from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import TaskModel

def index(request):
    tasks = TaskModel.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)

        try:
            if form.is_valid():
                form.save()
                return redirect('/')
        except Exception as e:
            
            print(f"Error saving form: {e}")

    else:
        form = TaskForm()

    return render(request, 'example/index.html', {
        'form': form,
        'tasks': tasks
    })

def UpdateView(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        try:
            form = TaskForm(request.POST, instance=task)

            if form.is_valid():
                form.save()
                return redirect('/')
        except Exception as e:
           
            print(f"Error updating form: {e}")

    else:
        form = TaskForm(instance=task)

    return render(request, 'example/update.html', {
        'form': form
    })

def DeleteView(request,pk):
    item=get_object_or_404(TaskModel,pk=pk)

    

    if request.POST:
        

        item.delete()
        return redirect('/')
    
    return render(request,'example/delete.html',{
        # 'form':form,
        'delete':item
    })



