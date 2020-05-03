from django.shortcuts import render, HttpResponse
from ajaxapp.models import Video


def hello(request):
    response = {'video': Video.objects.all()}
    return render(request, 'meet.html', response)


def adding_like(request):
    video = Video.objects.get(id=request.GET["id"])
    video.likes += 1
    video.save()
    return HttpResponse(video.likes)
