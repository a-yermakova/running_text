import io
from unittest import mock

import pytest
from django.test import Client
from django.urls import reverse

from app.models import History

client = Client()


@pytest.mark.django_db
def test_runtext_view_can_return_response():
    test_text = 'Спасибо, что откликнулись на стажировку!'
    test_file = io.StringIO(test_text)
    with mock.patch("app.service_layer.create_video_from_string") as mocked_method:
        mocked_method.return_value = test_file
        response = client.get(reverse('runtext'),{'text': test_text}, content_type='application/json')
        mocked_method.assert_called_once()

    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'video/mp4'
    print(History.objects.all())
    assert History.objects.filter(request_text=test_text).exists() is True
