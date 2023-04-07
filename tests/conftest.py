from app import server
from unittest.mock import patch
import json
import pytest
import os

CLUB_DB_TEST_PATH = os.path.join(os.path.dirname(__file__), "data", "clubs.json")
COMPETITION_BD_TEST_PATH = os.path.join(os.path.dirname(__file__), "data", "competitions.json")

TEST_CLUBS = [
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

TEST_COMPETITIONS = [
    {
        "name": "competition1",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "5"
    },
    {
        "name": "competition2",
        "date": "2025-03-27 10:00:00",
        "numberOfPlaces": "0"
    },
    {
        "name": "competition2",
        "date": "2025-03-27 10:00:00",
        "numberOfPlaces": "0"
    },
    {
        "name": "competition3",
        "date": "2025-03-27 10:00:00",
        "numberOfPlaces": "5"
    },
]


def club_mock(data: dict):
    # overwrite club datas
    db_test = open(CLUB_DB_TEST_PATH, "w")
    db_test.write(json.dumps(data, indent=4))  # type: ignore
    db_test.close()

    # return a mock of the club database path
    return patch('app.server.CLUB_DB_PATH', CLUB_DB_TEST_PATH)


def competition_mock(data: dict):
    # overwrite club datas
    db_test = open(COMPETITION_BD_TEST_PATH, "w")
    db_test.write(json.dumps(data, indent=4))
    db_test.close()

    # return a mock of the club database path
    return patch('app.server.COMPETITION_DB_PATH', COMPETITION_BD_TEST_PATH)


@pytest.fixture
def client():
    yield server.app.test_client()
