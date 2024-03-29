from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


# Create your views here.


def todoView(request):
    context = {
        'all_items': TodoItem.objects.all(),
    }
    return render(request, 'todo.html', context)


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    item = TodoItem.objects.get(id=todo_id)
    item.delete()
    return HttpResponseRedirect('/todo/')
