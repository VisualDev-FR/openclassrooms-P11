from app import server
from unittest.mock import patch
import json
import pytest
import os

CLUB_DB_TEST_PATH = os.path.join(os.path.dirname(__file__), "data", "clubs.json")
COMPETITION_BD_TEST_PATH = os.path.join(os.path.dirname(__file__), "data", "competitions.json")


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
