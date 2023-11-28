from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET

from app.service_layer import runtext_service


@require_GET
def runtext(request: WSGIRequest) -> HttpResponse | JsonResponse:
    try:
        video_data = runtext_service(request.GET.get('text', ''))
        response = HttpResponse(video_data, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename="your_video.mp4"'
        return response
    except Exception as e:
        return JsonResponse({'message': str(e)})
