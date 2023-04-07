from app import server
from tests import conftest
import pytest


@pytest.fixture
def dummy_club():
    return conftest.club_mock(data={
        "clubs": [
            {
                "name": "dummy_name",
                "email": "dummy@adress.co",
                "points": "13"
            },
        ],
    })


def test_load_clubs(dummy_club):

    with dummy_club:

        clubs = server.loadClubs()

        assert len(clubs) == 1
        assert clubs[0]['name'] == "dummy_name"
        assert clubs[0]['email'] == "dummy@adress.co"
        assert int(clubs[0]['points']) == 13


@pytest.fixture
def dummy_competition():
    return conftest.competition_mock(data={
        "competitions": [
            {
                "name": "dummy_competition",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25"
            },
        ]
    })


def test_load_competitions(dummy_competition):

    with dummy_competition:

        competitions = server.loadCompetitions()

        assert len(competitions) == 1

        assert competitions[0]['name'] == "dummy_competition"
        assert competitions[0]['date'] == "2020-03-27 10:00:00"
        assert int(competitions[0]['numberOfPlaces']) == 25
