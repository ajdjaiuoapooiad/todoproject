
from django.urls import path
from . import views


app_name='todo'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('create/',views.CreateView.as_view(),name='create'),
    path('detail/<int:pk>',views.DetailView.as_view(),name='detail'),
    path('delete/<int:pk>',views.DeleteView.as_view(),name='delete'),
    path('update/<int:pk>',views.UpdateView.as_view(),name='update'),
]
