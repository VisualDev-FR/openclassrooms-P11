from app import server


def test_load_clubs(clubs_mock_json):

    with clubs_mock_json:

        clubs = server.loadClubs()

        assert len(clubs) == 3
        assert clubs[0]['name'] == "club_1"
        assert clubs[0]['email'] == "club1@domain.co"
        assert int(clubs[0]['points']) == 5


def test_load_competitions(competitions_mock_json):

    with competitions_mock_json:

        competitions = server.loadCompetitions()

        assert len(competitions) == 4

        assert competitions[0]['name'] == "past_competition"
        assert competitions[0]['date'] == "2020-03-27 10:00:00"
        assert int(competitions[0]['numberOfPlaces']) == 5
