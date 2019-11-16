from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    return render(request,'index.html')

def introduce(request):
    intro = Post.objects.all()
    return render(request, 'detail.html', {'intro':intro})