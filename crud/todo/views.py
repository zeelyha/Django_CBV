from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TodoApp

# Create your views here.
class TodoAppCreateView(CreateView):

    #specify the model to create view
    model = TodoApp

    #specify the fields to be displayed
    fields = ["title", "description"]
    template_name = 'home.html'
    success_url = 'list.html'


class TodoAppListView(ListView):
    model = TodoApp
    template_name = 'list.html'


class TodoAppDetailView(DetailView):
    model = TodoApp
    template_name = 'detail.html'


class TodoAppUpdateView(UpdateView):
    model = TodoApp
    fields = ['title', 'description']
    template_name = 'update.html'
    success_url = '/'


class TodoAppDeleteView(DeleteView):
    model = TodoApp
    template_name = 'delete.html'
    success_url = '/'