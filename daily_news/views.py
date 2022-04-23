from django.shortcuts import render,redirect
from django.http import Http404
from .models import News
from.forms import NewsForm


def news_detail_view(request, id=None):
    news_obj = None
    if id is not None:
        try:
            news_obj = News.objects.get(id=id)
        except News.DoesNotExist:
            raise Http404
    context = {
        'news':news_obj
    }
    return render(request, 'daily_news/details.html', context)

def news_create_view(request):
    form = NewsForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        context['form'] = NewsForm()
        news_obj = form.save()
        return redirect(news_obj.get_absolute_url())
    return render(request, 'daily_news/create.html', context)