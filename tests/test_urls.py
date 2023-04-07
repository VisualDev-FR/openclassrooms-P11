from flask.testing import FlaskClient


def test_get_login_url(client: FlaskClient):

    response = client.get("/")

    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data