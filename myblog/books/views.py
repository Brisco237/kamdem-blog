from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Books
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from django.db.models import Q

# Create your views here.
class BooksListView(ListView):
    paginate_by = 18
    model = Books
    template_name = 'book/bookslist.html'
    queryset = Books.objects.all().order_by('-date_add')
    context_object_name = 'object_list'

    def get_queryset(self):
        query = self.request.GET.get('q', '')  # Récupère le terme de recherche
        if query:
            # Filtrer par titre, auteur, ou nom de catégorie
            return Books.objects.filter(
                title__icontains=query
            ) | Books.objects.filter(
                author__icontains=query
            ) | Books.objects.filter(
                category__name__icontains=query  # Recherche sur le nom de la catégorie
            )
        return Books.objects.all()  # Si pas de recherche, afficher tous les livres

#@permission_required('books.view_book', raise_exception=True)
class BooksDetailsView(LoginRequiredMixin, DetailView):
    model = Books
    template_name = 'book/booksdetails.html'
    redirect_field_name = 'next'


