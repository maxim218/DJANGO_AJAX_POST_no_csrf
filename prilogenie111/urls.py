from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.my_main_page, name='my_main_page'),
    url(r'^get_proizved/', views.get_proizved, name='get_proizved'),
    url(r'^hello_query/', views.hello_query, name='hello_query'),
]