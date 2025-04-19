from urllib import request
from articles.models import Articles
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
#from django.contrib.auth.decorators import permission_required
from django.db.models import Count, Q
from .models import Comments
from django.contrib import messages


# Create your views here.
class ArticlesListView(ListView):
    paginate_by = 10
    model = Articles
    template_name = 'articles/articleslist.html'
    context_object_name = 'articleslist'

    def get_queryset(self):
        #Réupere le nombre de commentaires
        queryset = Articles.objects.annotate(comment_count=Count("commentaires"))
    
        query = self.request.GET.get("q")  # Récupère le mot tapé par l'utilisateur
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |  # Cherche dans le titre
                Q(content__icontains=query) |  # Cherche dans le contenu
                Q(author__username__icontains=query)  # Cherche dans le nom de l'auteur
            )
        return queryset
    
#@permission_required('articles.view_article', raise_exception=True)
class ArticlesDetailsView(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = 'articles/articlesdetails.html'
    #context_object_name = 'articlesdetails'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        # Récupérer le contexte initial de Django
        context = super().get_context_data(**kwargs)
        # Ajouter la liste des commentaires associés à l'article
        context['commentaires'] = self.object.commentaires.all().order_by('-date_add')
        return context
        
    
    def post(self, request, *args, **kwargs):
        # Récupérer l'article
        self.object = self.get_object()
        # Extraire les données du formulaire
        content = request.POST.get("commentaire")
        if content:
            # Créer un commentaire
            Comments.objects.create(article=self.object, author=request.user, content=content)
            messages.success = 'Votre commentaire a bien été ajouté.'
        # Rediriger après soumission
        return redirect('articlesdetails', pk=self.object.pk)
    

