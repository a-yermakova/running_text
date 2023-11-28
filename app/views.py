from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET

from app.service_layer import runtext_service


@require_GET
def runtext(request):
    string = request.GET.get('text', '')
    try:
        video_data = runtext_service(request, string)
        response = HttpResponse(video_data, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename="your_video.mp4"'
        return response
    except Exception as e:
        return JsonResponse({'message': str(e)})
