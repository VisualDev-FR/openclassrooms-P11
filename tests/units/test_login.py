from flask.testing import FlaskClient


def test_get_login_url(client: FlaskClient):

    response = client.get("/")

    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data


def test_login_with_valid_credentials(client: FlaskClient, clubs_mock):

    with clubs_mock:

        response = client.post(
            "/showSummary",
            data={
                "email": "club1@domain.co"
            }
        )

        assert response.status_code == 200
        assert b"Welcome to the GUDLFT Registration Portal!" not in response.data
        assert b"Welcome, club1@domain.co" in response.data


def test_login_with_invalid_credentials(client: FlaskClient, clubs_mock):

    with clubs_mock:

        response = client.post(
            "/showSummary",
            data={
                "email": "invalid@adress.co"
            }
        )

        assert response.status_code == 200
        assert b"Welcome to the GUDLFT Registration Portal!" in response.data


def test_logout(client: FlaskClient):

    response = client.get("/logout", follow_redirects=True)

    assert response.status_code in [200, 302]
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data    