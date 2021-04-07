
from django.urls import path
from . import views
app_name='ytyoutube'
urlpatterns = [
    path('',views.youtube, name='youtube'),
    path('download/',views.download, name='download'),
    path('download/<resolution>/',views.yt_download, name='yt_downloaddone'),
]
