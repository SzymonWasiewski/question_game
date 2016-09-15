from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from categories import views

urlpatterns = [
    url(r'^categories/$', views.CategoryList.as_view(), name='categories_list'),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view(), name='category_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)