from django.contrib.syndication.views import Feed
from .models import Post
from django.template.defaultfilters import truncatewords_html


class CheckLatestPosts(Feed):
    title = 'Bikalpa Codes'
    link = '/blog/'
    description = 'New posts in Bikalpa Codes'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self):
        return self.title

    def item_description(self):
        return truncatewords_html(self.description, 30)
