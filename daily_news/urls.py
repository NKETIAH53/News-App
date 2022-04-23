from django.urls import path
from .views import news_detail_view, news_create_view
from news.views import home_view




app_name = 'daily_news'

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', news_create_view, name='create'), 
    path('<int:id>/', news_detail_view, name='detail')
]
