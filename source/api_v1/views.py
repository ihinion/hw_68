import json

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie

from api_v1.serializers import ArticleSerializer
from webapp.models import Article


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        object = get_object_or_404(Article, pk=kwargs.get('pk'))
        slr = ArticleSerializer(object)
        return JsonResponse(slr.data, safe=False)


class ArticleCreateView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        slr = ArticleSerializer(data=data)
        if slr.is_valid():
            slr.save()
            return JsonResponse(slr.data, safe=False)
        else:
            response = JsonResponse(slr.errors, safe=False)
            response.status_code = 400
            return response


class ArticleUpdateView(View):
    def put(self, request, *args, **kwargs):
        object = get_object_or_404(Article, pk=kwargs.get('pk'))
        data = json.loads(request.body)
        slr = ArticleSerializer(data=data, instance=object)
        if slr.is_valid():
            slr.save()
            return JsonResponse(slr.data, safe=False)
        else:
            response = JsonResponse(slr.errors, safe=False)
            response.status_code = 400
            return response


# class ArticleCreateView(View):
#     def post(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             response = JsonResponse({
#                 'error': 'Forbidden'
#             })
#             response.status_code = 403
#             return response
#         data = json.loads(request.body)
#         print(data)
#         article = Article.objects.create(
#             author=self.request.user,
#             title=data['title'],
#             text=data['text']
#         )
#         return JsonResponse({
#             'pk': article.pk,
#             'author': article.author_id,
#             'title': article.text,
#             'text': article.text,
#             'created_at': article.created_at.strftime('%Y-%m-%d %H:%M:%S'),
#             'updated_at': article.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
#         })


class ArticleListView(View):
    def get(self, request, *args, **kwargs):
        objects = Article.objects.all()
        slr = ArticleSerializer(objects, many=True)
        return JsonResponse(slr.data, safe=False)


class ArticleDeleteView(View):
    def delete(self, request, *args, **kwargs):
        object = get_object_or_404(Article, pk=kwargs.get('pk'))
        obj_id = object.id
        object.delete()
        return JsonResponse({'id': obj_id}, safe=False)