import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_201_CREATED

from polls.models import Poll


@pytest.mark.django_db
def test_polls_get(api_client, polls_factory):
    poll = polls_factory()
    url = reverse("polls-detail", args=(poll.id,))
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK

    resp_json = resp.json()
    assert resp_json['id'] == poll.id


@pytest.mark.django_db
def test_polls_list(api_client, polls_factory):
    poll = polls_factory()
    url = reverse("polls-list")
    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_filter_id(api_client, polls_factory):
    poll = polls_factory(_quantity=3)
    url = reverse("polls-list")
    resp = api_client.get(url, {'id': poll[0].id})
    assert resp.status_code == HTTP_200_OK

    resp_json = resp.json()
    assert len(resp_json) == 3


@pytest.mark.django_db
def test_poll_filter_name(api_client):
    poll = Poll.objects.bulk_create([
        Poll(title='two poll'),
        Poll(title='one poll'),
    ])
    url = reverse("polls-list")
    resp = api_client.get(url, {'title': 'one poll'})
    assert resp.status_code == HTTP_200_OK

    resp_json = resp.json()
    assert len(resp_json) == 2
    resp_poll = resp_json[1]
    assert resp_poll['title'] == poll[1].title



