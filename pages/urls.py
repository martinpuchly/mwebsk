from django.urls import path
from . import views

urlpatterns = [
    path('clanky', views.post_index, name='posts'),
    path('clanky/<slug:tag>', views.post_tag_index, name='posts.tag'),
    path('clanok/<slug:post_slug>', views.post_show, name='post.show'),
    path('<slug:page_slug>', views.page_show, name='page.show'),

]

