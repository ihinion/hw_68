from django.urls import path

from api_v1.views import get_token_view, ArticleCreateView

app_name = 'api_v1'

urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('article-create/', ArticleCreateView.as_view(), name='article_create')
]