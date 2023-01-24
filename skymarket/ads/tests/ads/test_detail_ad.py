import pytest


@pytest.mark.django_db
def test_detail_ads(user_client, ad):
    expected_response = {
        "pk": ad.pk,
        "image": None,
        "title": "test_title",
        "price": 1000,
        "phone": "+79995553311",
        "description": "test_description",
        "author_first_name": "test_name",
        "author_last_name": "test_last_name",
        "author_id": ad.author.id
    }

    response = user_client.get(f"/api/ads/{ad.pk}/")

    assert response.status_code == 200
    assert response.data == expected_response

@pytest.mark.django_db
def test_is_authorization(client, ad):
    response = client.get(f"/api/ads/{ad.pk}/")

    assert response.status_code == 401