from django.urls import path
from .views import ArticlesListView, ArticlesDetailsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('articles/', ArticlesListView.as_view(), name='articleslist'),
    path('articles/articlesdetails/<int:pk>/', ArticlesDetailsView.as_view(), name='articlesdetails'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
