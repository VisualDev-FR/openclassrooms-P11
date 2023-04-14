from flask.testing import FlaskClient
from unittest.mock import patch, _patch
import pytest


@pytest.fixture
def purchase_clubs_mock():
    return patch('app.server.clubs', [
        {
            "name": "club_1",
            "email": "club1@domain.co",
            "points": "13"
        },
    ])


@pytest.fixture
def purchase_competitions_mock():
    return patch('app.server.competitions', [
        {
            "name": "competition1",
            "date": "2099-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
    ])


def test_purchase_decrements(client: FlaskClient, purchase_competitions_mock: _patch, purchase_clubs_mock: _patch):

    with purchase_competitions_mock, purchase_clubs_mock:

        response = client.post(
            "/purchasePlaces",
            data={
                "club": "club_1",
                "competition": "competition1",
                "places": 2,
            }
        )

        assert response.status_code == 200
        assert b"Points available: 11" in response.data
        assert b"Number of Places: 23" in response.data
        assert b"Great-booking complete!" in response.data
        assert b"You cannot book more than 12 places." not in response.data


def test_purchase_more_than_12_places(client: FlaskClient, purchase_clubs_mock: _patch, purchase_competitions_mock: _patch):

    with purchase_competitions_mock, purchase_clubs_mock:

        response = client.post(
            "/purchasePlaces",
            data={
                "club": "club_1",
                "competition": "competition1",
                "places": 13,
            }
        )

        assert response.status_code == 200
        assert b"Points available: 1" in response.data
        assert b"Number of Places: 13" in response.data
        assert b"You cannot book more than 12 places." in response.data
        assert b"Great-booking complete!" not in response.data
