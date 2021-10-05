from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
import random



def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response(We pick to 	return the response)
    """
    id = random.randint(1,25)
    # obj = Article(title = "I am title5", content="Hi, i am context5")
    Article_obj = Article.objects.get(id = id)
    article_queryset = Article.objects.all()
   
    context = {
        "object_list": article_queryset,
        "title1": Article_obj.title,
        "context1": Article_obj.content,
        "id": Article_obj.id
    }
    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context = context)
   
    # HTML_STRING = """
	# <h1>{title1}</h1>
    # <p>{context1}</p>
    
	# """.format(**context)

    return HttpResponse(HTML_STRING)

