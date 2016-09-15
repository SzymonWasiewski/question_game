from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from questions import views

urlpatterns = [
    url(r'^questions/$', views.QuestionList.as_view(), name='questions_list'),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(), name='question_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)