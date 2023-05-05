from flask.testing import FlaskClient


def test_past_competitions_are_not_bookable(client: FlaskClient, clubs_mock, competitions_mock):

    with clubs_mock, competitions_mock:

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


def test_future_competitions_are_bookable(client: FlaskClient, clubs_mock, competitions_mock):

    with clubs_mock, competitions_mock:

        response = client.post(
            "/showSummary",
            data={
                "email": "club1@domain.co"
            }
        )

        assert response.status_code == 200
        assert b"future_competition_0_places" in response.data
        assert b"2099-03-27 10:00:00" in response.data
        assert b"Number of Places: 0" in response.data
