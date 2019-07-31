from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^signup/$', registration),
    url(r'^signup1',signup),
    url(r'^searchdata/$',searchdata)

]
