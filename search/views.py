from django.shortcuts import render
from search.documents import PostDocument

def search(request):
    q = request.GET.get('q')
    if q:
        posts = PostDocument.search().query("match", title=q)
    else:
        posts = ''
    return render(request, 'search/search.html', {'posts': posts})
