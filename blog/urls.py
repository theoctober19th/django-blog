from django.urls import path
from .views import post_list, post_detail

# this defines the application namespace
app_name = 'blog'

urlpatterns = [
    path('', post_list, name='list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>',
         post_detail, name='detail'),
]
