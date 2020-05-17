from django.shortcuts import render, redirect
from .models import Article
import datetime

# Create your views here.

def movie_in_view(request):
    movie_list=Article.objects.filter(category='movie')
    return render(request, 'movie.html', {'ml':movie_list})

def drama_in_view(request):
    drama_list=Article.objects.filter(category='drama')
    return render(request, 'drama.html', {'dl':drama_list})

def entertain_in_view(request):
    entertain_list=Article.objects.filter(category='entertain')
    return render(request, 'entertain.html', {'el':entertain_list})



def index_defined_in_view(request):
    movie_count=Article.objects.filter(category='movie').count()
    drama_count=Article.objects.filter(category='drama').count()
    entertatin_count=Article.objects.filter(category='entertain').count()
    return render(request,'index_in_templates.html', {'mc':movie_count, 'dc':drama_count, 'ec':entertatin_count})

def detail_defined_in_view(request, primary_key_of_the_name_that_i_clicked):
    article = Article.objects.get(pk=primary_key_of_the_name_that_i_clicked)
    return render(request, 'detailed_in_templates.html', {'a_article_i_will_use_in_html':article})

def new_defined_in_view(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            time = datetime.datetime.now()

            # time은 맨 위에서 import datetime을 함으로써 저렇게 실시간으로 가지고 올 수 있음  
        )
        return redirect('detail_i_will_use_in_html', primary_key_of_the_name_that_i_clicked=new_article.pk)
    else:
        return render(request, 'new_in_templates.html')
