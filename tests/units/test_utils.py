from app import utils
from tests.conftest import TEST_COMPETITIONS


def test_get_past_competitions():
    past_competitions = utils.get_past_competitions(TEST_COMPETITIONS)
    assert len(past_competitions) == 1


def test_get_future_competitions():
    future_competitions = utils.get_future_competitions(TEST_COMPETITIONS)
    assert len(future_competitions) == 3
