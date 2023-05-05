from app import server
from unittest.mock import patch
import json
import pytest
import os

CLUB_DB_PATH_TEST = os.path.join(os.path.dirname(__file__), "data", "clubs.json")
COMPETITION_DB_PATH_TEST = os.path.join(os.path.dirname(__file__), "data", "competitions.json")

TEST_CLUBS = {
    "clubs": [
        {
            "name": "club_1",
            "email": "club1@domain.co",
            "points": "5"
        },
        {
            "name": "club_2",
            "email": "club2@domain.co",
            "points": "15"
        },
        {
            "name": "club_3",
            "email": "club3@domain.co",
            "points": "20"
        }
    ]
}

TEST_COMPETITIONS = {
    "competitions": [
        {
            "name": "past_competition",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "5"
        },
        {
            "name": "future_competition_0_places",
            "date": "2099-03-27 10:00:00",
            "numberOfPlaces": "0"
        },
        {
            "name": "future_competition_10_places",
            "date": "2099-03-27 10:00:00",
            "numberOfPlaces": "10"
        },
        {
            "name": "future_competition_15_places",
            "date": "2099-03-27 10:00:00",
            "numberOfPlaces": "15"
        },
    ]
}


@pytest.fixture
def clubs_mock():
    return patch('app.server.clubs', TEST_CLUBS['clubs'])


@pytest.fixture
def competitions_mock():
    return patch('app.server.competitions', TEST_COMPETITIONS['competitions'])


@pytest.fixture
def clubs_mock_json():
    # overwrite club datas
    db_test = open(CLUB_DB_PATH_TEST, "w")
    db_test.write(json.dumps(TEST_CLUBS, indent=4))  # type: ignore
    db_test.close()

    # return a mock of the club database path
    return patch('app.server.CLUB_DB_PATH', CLUB_DB_PATH_TEST)


@pytest.fixture
def competitions_mock_json():
    # overwrite club datas
    db_test = open(COMPETITION_DB_PATH_TEST, "w")
    db_test.write(json.dumps(TEST_COMPETITIONS, indent=4))
    db_test.close()

    # return a mock of the club database path
    return patch('app.server.COMPETITION_DB_PATH', COMPETITION_DB_PATH_TEST)


@pytest.fixture
def client():
    yield server.app.test_client()
