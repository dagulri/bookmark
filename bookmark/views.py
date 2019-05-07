from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark


class BookmarkCreateView(CreateView):
        model = Bookmark
        fields = ['site_name','url']
        success_url = reverse_lazy('list')
        template_name_suffix = '_create'

class BookmarkListView(ListView):
        model = Bookmark
        paginate_by = 6

class BookmarkDetailView(DetailView):
        model = Bookmark

class BookmarkUdateView(UpdateView):
        model = Bookmark
        fields = ['site_name','url']
        template_name_suffix = '_update'
        success_url = reverse_lazy('list')

class BookmarkDeleteView(DeleteView):
        model = Bookmark
        success_url = reverse_lazy('list')



# Create your views here.
