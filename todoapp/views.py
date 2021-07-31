from django.shortcuts import render
from  .models import Todo
from django import forms

class TodoForm(forms.Form):
    todo = forms.CharField(max_length=80)


def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_item = form.cleaned_data['todo']

            todo = Todo(todo_item=todo_item)
            todo.save()


    todos = Todo.objects.all()
    context = {"todos": todos, "my_form": TodoForm()}
    return render(request, 'todoapp/index.html', context)