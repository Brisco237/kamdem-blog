from django.urls import path
from .views import BooksListView, BooksDetailsView, DetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('books/bookslist/',BooksListView.as_view(),name='bookslist'),
    path('books/booksdetails/<int:pk>/',BooksDetailsView.as_view(),name='booksdetails'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)