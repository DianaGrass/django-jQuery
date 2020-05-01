from django.urls import path
from ajaxapp.views import hello, adding_like


urlpatterns = [
    path('', hello),
    path("add_like/", adding_like),
]
