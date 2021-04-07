from django.shortcuts import (render,HttpResponseRedirect , get_object_or_404 )
from .models import Article
from .forms import article_form


def search(request, query):
    if request.method == "GET":
        query = request.GET.get('query', None)
        if query:
            results = Article.objects.filter(title__icontains=query | content__icontains=query)
            context = {'results':results}
            return render(request, 'article-search.html', context)



def create_article(request):
    article = Article.objects.all()
    if request.method =='PPOST':
        form =art(request.POST)
    if form.is_valid():
        article=form.save(comit=False)

        article.title = title
        article.user = user
        article.created_at = created_at
        article.content = content
        article.down_votes = down_votes
        article.updated_at = apdated_at
        article.up_votes = up_votes

        article.save()
    else:
        form = art()
    return render(request, "create_topic.html",{'article':article})



def delete_article(request, id):
    context = {}
    obj = get_object_or_404(Article,id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete_article.html", context)


def update_view(request, id):

    context = {}

    obj = get_object_or_404(Article, id=id)

    # pass the object as instance in form
    form = article_form(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    context["form"] = form

    return render(request, "update_article.html", context)