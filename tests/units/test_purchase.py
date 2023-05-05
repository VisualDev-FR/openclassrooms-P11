from flask.testing import FlaskClient


def test_purchase_decrements(client: FlaskClient, clubs_mock, competitions_mock):

    with clubs_mock, competitions_mock:

        response = client.post(
            "/purchasePlaces",
            data={
                "club": "club_1",
                "competition": "future_competition_10_places",
                "places": 2,
            }
        )

        assert response.status_code == 200
        assert b"Points available: 3" in response.data
        assert b"Number of Places: 8" in response.data
        assert b"Great-booking complete!" in response.data
        assert b"You cannot book more than 12 places." not in response.data


def test_purchase_more_than_12_places(client: FlaskClient, clubs_mock, competitions_mock):

    with clubs_mock, competitions_mock:

        response = client.post(
            "/purchasePlaces",
            data={
                "club": "club_1",
                "competition": "future_competition_15_places",
                "places": 13,
            }
        )

        assert response.status_code == 200
        assert b"You cannot book more than 12 places." in response.data


def test_purchase_more_places_than_available_points(client: FlaskClient, clubs_mock, competitions_mock):

    with clubs_mock, competitions_mock:

        response = client.post(
            "/purchasePlaces",
            data={
                "club": "club_1",
                "competition": "future_competition_15_places",
                "places": 10,
            },
        )

        assert response.status_code == 200
        assert b"You don&#39;t have enought points" in response.data
