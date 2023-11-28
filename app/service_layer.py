import os
import cv2
import json
import numpy as np

from PIL import ImageFont, Image, ImageDraw
from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest

from app.models import History


def runtext_service(request: WSGIRequest, runtext_vo):
    video_response = create_video_from_string(runtext_vo)

    History.objects.create(
        request_url=request.get_full_path(),
    )

    return video_response


def create_video_from_string(string_variable):
    width, height = 100, 100
    fps = 30
    duration = 3

    font = ImageFont.truetype("fonts/calibri.ttf", 35)
    text_color = (255, 255, 255)
    speed_factor = 1.3

    output_file = 'output.mp4'

    frames = np.zeros((duration * fps, height, width, 3), dtype=np.uint8)

    text_width = font.getlength(text=string_variable)
    speed = text_width * speed_factor / duration

    for i in range(duration * fps):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        text_position_x = int(width - (i / fps) * speed)
        text_position_y = (height) // 2
        image = Image.fromarray(frame)
        draw = ImageDraw.Draw(image)
        draw.text((text_position_x, text_position_y), string_variable, font=font, fill=text_color)
        frame = np.array(image)
        frames[i] = frame

    temp_dir = 'temp_frames'
    os.makedirs(temp_dir, exist_ok=True)
    for i, frame in enumerate(frames):
        cv2.imwrite(f'{temp_dir}/{i:04d}.png', frame)

    os.system(f'ffmpeg -framerate {fps} -i "{temp_dir}/%04d.png" -c:v libx264 -pix_fmt yuv420p {output_file}')

    video_path = os.path.join(settings.MEDIA_ROOT, output_file)
    with open(video_path, 'rb') as video_file:
        video_data = video_file.read()

    # os.system(f'rm -rf {temp_dir}')
    os.system(f'rd /Q/s {temp_dir}')
    os.system(f'del {output_file}')
    return video_data
