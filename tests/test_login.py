from flask.testing import FlaskClient
from tests import conftest
import pytest


def test_get_login_page(client: FlaskClient):

    response = client.get("/")

    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data


@pytest.fixture
def dummy_club():
    return conftest.club_mock(data={
        "clubs": [
            {
                "name": "dummy_name",
                "email": "valid@adress.co",
                "points": "13"
            },
        ],
    })


def test_login_with_valid_credentials(client: FlaskClient, dummy_club):

    with dummy_club:

        response = client.post(
            "/showSummary",
            data={
                "email": "valid@adress.co"
            }
        )

        assert response.status_code == 200
        assert b"Welcome, valid@adress.co" in response.data


def test_login_with_invalid_credentials(client: FlaskClient, dummy_club):

    with dummy_club:

        response = client.post(
            "/showSummary",
            data={
                "email": "invalid@adress.co"
            }
        )

        assert response.status_code == 200
        assert b"Welcome to the GUDLFT Registration Portal!" in response.data
