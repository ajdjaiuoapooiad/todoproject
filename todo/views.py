from django.shortcuts import render
from .models import Post
from django.views import generic
from .forms import PostCreateForm

class IndexView(generic.ListView):
    model=Post
    
class CreateView(generic.CreateView): 
    model=Post
    form_class=PostCreateForm
    
    def __str__(self):
        return self.title