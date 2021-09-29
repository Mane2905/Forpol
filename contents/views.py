from django.shortcuts import render,get_object_or_404
from .models import Content
# Create your views here.
def index(request):
    contents=Content.objects.order_by('-Date').filter(is_published=True)
    context={
        'contents':contents,
    }
    return render(request, 'index.html',context)
def content(request,content_id):
    content=get_object_or_404(Content,pk=content_id)
    context={
        'content':content
    }
    return render(request,'content.html',context)