from datetime import datetime


def get_past_competitions(competitions_list: list):
    return [
        comp for comp in competitions_list if
        datetime.fromisoformat(comp['date']) < datetime.now()
    ]


def get_future_competitions(competitions_list: list):
    return [
        comp for comp in competitions_list if
        datetime.fromisoformat(comp['date']) > datetime.now()
    ]
