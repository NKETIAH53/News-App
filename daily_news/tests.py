from django.test import TestCase
from .models import News

class NewsTestCase(TestCase):
    def setUp(self):
        News.objects.create(title = 'Hey', content= 'Hello World')
        
    def test_news_queryset_exists(self):
        queryset = News.objects.all()
        self.assertTrue(queryset.exists())

    def test_news_queryset_count_isOne(self):
        queryset = News.objects.all()
        self.assertEqual(queryset.count(), 1)
        
    def test_news_queryset_count_not_more_thanOne(self):
        queryset = News.objects.all()
        self.assertNotEqual(queryset.count(), 2)
