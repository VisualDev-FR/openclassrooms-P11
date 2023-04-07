from flask.testing import FlaskClient
from unittest.mock import patch
import pytest


@pytest.fixture
def past_competitions_only():
    return patch('app.server.competitions', [
        {
            "name": "past_competition",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "5"
        },
    ])


@pytest.fixture
def future_competitions_only():
    return patch('app.server.competitions', [
        {
            "name": "future_competition",
            "date": "2099-03-27 10:00:00",
            "numberOfPlaces": "5"
        },
    ])


def test_past_competitions_are_not_bookable(client: FlaskClient, variable_clubs_mock, past_competitions_only):

    with variable_clubs_mock, past_competitions_only:

        response = client.post(
            "/showSummary",
            data={
                "email": "club1@domain.co"
            }
        )

        assert response.status_code == 200
        assert b"past_competition" in response.data
        assert b"2020-03-27 10:00:00" in response.data
        assert b"Number of Places: 5" not in response.data


def test_future_competitions_are_bookable(client: FlaskClient, variable_clubs_mock, future_competitions_only):

    with variable_clubs_mock, future_competitions_only:

        response = client.post(
            "/showSummary",
            data={
                "email": "club1@domain.co"
            }
        )

        assert response.status_code == 200
        assert b"future_competition" in response.data
        assert b"2099-03-27 10:00:00" in response.data
        assert b"Number of Places: 5" in response.data
