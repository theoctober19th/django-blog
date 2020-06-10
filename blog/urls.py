from django.urls import path
from .views import post_list, post_detail, post_share
from .views import PostListView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
from .feeds import CheckLatestPosts

# this defines the application namespace
app_name = 'blog'

sitemaps = {
    'posts': PostSitemap
}
post_feed = CheckLatestPosts()

urlpatterns = [
    path('', post_list, name='post_list'),
    path('/tag/<slug:tag_slug>/', post_list, name='post_list_with_tag'),
    # path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>',
         post_detail, name='detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', post_feed, name='post_feed'),
]
