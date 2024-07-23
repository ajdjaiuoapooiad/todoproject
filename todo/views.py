from django.urls import reverse_lazy
from .models import Post
from django.views import generic
from .forms import PostCreateForm

class IndexView(generic.ListView):
    model=Post
    
class CreateView(generic.CreateView): 
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy('todo:index')
    
    def __str__(self):
        return self.title