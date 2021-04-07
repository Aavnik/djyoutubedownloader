from django.shortcuts import render
from pytube import YouTube
import os

# Create your views here.

def youtube (request):
    return render(request, 'youtube/home.html')
def download (request):
    global url
    url = request.GET.get('ytlink')
    yt = YouTube(url)
    videos= []
    videos= yt.streams.filter(progressive=True).all()
    embed_link = url.replace("watch?v=","embed/")
    Title = yt.title
    context = {'videos':videos, 'embed':embed_link,'title':Title}

    return render(request, 'youtube/download.html', context)
def yt_download(request, resolution):
    global url
    homedir = os.path.expanduser("~")
    dir= homedir = 'Downloads'
    print(dir)
    if request.method =='POST':
        YouTube(url).streams.get_by_resolution(resolution).download(dir)
        
        
        return render(request, 'youtube/done.html')
    else:
        return render(request, 'youtube/error.html')



   