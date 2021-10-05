from django.shortcuts import render
from .models import Article

# Create your views here.

def article_detail_view(request, id=None):
    Article_obj = None
    if id is not None:
        Article_obj = Article.objects.get(id = id)
    context = {
        "object": Article_obj,
    }
    return render(request, "articles/detail.html", context = context)
