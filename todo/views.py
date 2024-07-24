from django.urls import reverse_lazy
from .models import Post
from django.views import generic
from .forms import PostCreateForm,PostUpdateForm

class IndexView(generic.ListView):
    model=Post
    
class CreateView(generic.CreateView): 
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy('todo:index')
    
    def __str__(self):
        return self.title
    
class DetailView(generic.DetailView):
    model=Post
    
    
class DeleteView(generic.DeleteView):
    model=Post
    success_url=reverse_lazy('todo:index')
    
class UpdateView(generic.UpdateView):
    model=Post
    form_class=PostUpdateForm
    success_url=reverse_lazy('todo:index')
    
    
    