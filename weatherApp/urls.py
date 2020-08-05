from django.conf.urls import url
from weatherApp import views
urlpatterns=[
url(r'^$',views.index),
]
