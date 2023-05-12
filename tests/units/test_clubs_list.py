from flask.testing import FlaskClient


def test_club_list_points_are_correct(client: FlaskClient, clubs_mock):

    with clubs_mock:

        response = client.get('/clubs')

        assert response.status_code == 200

        assert b"club_1 : 5 points" in response.data
        assert b"club_2 : 15 points" in response.data
        assert b"club_3 : 20 points" in response.data
