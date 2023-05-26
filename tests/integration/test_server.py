from flask.testing import FlaskClient
from app import server as app


def test_server(client: FlaskClient, clubs_mock, competitions_mock):

    with clubs_mock, competitions_mock:

        # assert that test datas are correctly loaded
        assert app.clubs[0]['name'] == "club_1"
        assert app.clubs[0]['email'] == "club1@domain.co"
        assert int(app.clubs[0]['points']) == 5

        # get the login page
        login = client.get('/')
        assert login.status_code == 200
        assert b"Welcome to the GUDLFT Registration Portal!" in login.data

        # login with club 1
        show_summary = client.post(
            "/showSummary",
            data={
                "email": "club1@domain.co"
            }
        )

        assert show_summary.status_code == 200
        assert b"past_competition" in show_summary.data
        assert b"2020-03-27 10:00:00" in show_summary.data
        assert b"Number of Places: 5" not in show_summary.data

        # select competition
        booking = client.get(r"/book/future_competition_10_places/club_1")

        assert booking.status_code == 200
        assert b'<input type="number" name="places" id="" max="12"/>' in booking.data

        # purchase places
        purchase = client.post(
            "/purchasePlaces",
            data={
                "club": "club_1",
                "competition": "future_competition_10_places",
                "places": 2,
            }
        )

        assert purchase.status_code == 200
        assert b"Points available: 3" in purchase.data
        assert b"Number of Places: 8" in purchase.data

        # logout
        logout = client.get("/logout", follow_redirects=True)

        assert logout.status_code in [200, 302]
        assert b"Welcome to the GUDLFT Registration Portal!" in logout.data


