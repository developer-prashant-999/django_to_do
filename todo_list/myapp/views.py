from django.shortcuts import render, redirect
from .models import ToDo

# List all ToDo items
def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

# Add a new ToDo item
def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        ToDo.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'todo/add_todo.html')

# Update a ToDo item
def complete_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

# Delete a ToDo item
def delete_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
