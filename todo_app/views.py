from django.shortcuts import render

from django.views.generic import ListView
from .models import ToDoList, ToDoItem


class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])
    
    def get_context_data(self):
        context = super().get_context_data()
        context["list_id"] = ToDoList.objects.get(self.kwargs["list_id"])
        return context