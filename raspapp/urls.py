from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from raspapp import views

urlpatterns = [

    url(r'test/', views.Test.as_view()),
    url(r'food/', views.food.as_view()),
    url(r'water/', views.water.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
