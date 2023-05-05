from flask.testing import FlaskClient


def test_ui_prevent_booking_more_than_12_places(client: FlaskClient, variable_clubs_mock, variable_competitions_mock):

    with variable_clubs_mock, variable_competitions_mock:

        response = client.get(r"/book/competition3/club_1")

        assert response.status_code == 200
        assert b'<input type="number" name="places" id="" max="12"/>' in response.data
