from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api.views import PostList,PostDetail
urlpatterns = [
   path('posts/',PostList.as_view(),name='post_list_view'),
   path('posts/<int:pk>',PostDetail.as_view(),name='post_detail_view')
]

urlpatterns = format_suffix_patterns(urlpatterns)