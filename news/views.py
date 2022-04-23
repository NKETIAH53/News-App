from django.shortcuts import render
from daily_news.models import News

def home_view(request):
    news_list = News.objects.all()
    print(news_list)
    context = {
        'news':news_list
    }
    return render(request, 'news/home.html', context)