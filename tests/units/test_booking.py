from flask.testing import FlaskClient


def test_ui_prevent_booking_more_than_12_places(client: FlaskClient, clubs_mock, competitions_mock):

    with clubs_mock, competitions_mock:

        response = client.get(r"/book/future_competition_10_places/club_1")

        assert response.status_code == 200
        assert b'<input type="number" name="places" id="" max="12"/>' in response.data
