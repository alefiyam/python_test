from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    url(r'^api/get_que_ans/$', views.get_que_ans ,name = 'get_api_que_ans'),
    url(r'^api/get_user_id/$', views.get_user_id ,name = 'get_user_id'),
    url(r'^api/dashboard/$', views.dashboard ,name = 'dashboard'),
    url(r'^api/term/$', views.get_que_by_search_term ,name = 'term')
]
urlpatterns = format_suffix_patterns(urlpatterns) 
