import pytest


@pytest.mark.django_db
def test_create_comment(user_client, ad, user_api):
    data = {
        "text": "test_text"
    }

    response = user_client.post(f"/api/ads/{ad.pk}/comments/", data)

    expected_response = {
        "pk": response.data.get("pk"),
        "text": "test_text",
        "author_id": user_api.pk,
        "created_at": response.data.get("created_at"),
        "author_first_name": "test name",
        "author_last_name": "test last_name",
        "ad_id": ad.pk,
        "author_image" : None
    }

    assert response.status_code == 201
    assert response.data == expected_response
