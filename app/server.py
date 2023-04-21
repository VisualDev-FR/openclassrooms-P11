from flask import Flask, render_template, request, redirect, flash, url_for
from app import utils
import json


CLUB_DB_PATH = "clubs.json"
COMPETITION_DB_PATH = "competitions.json"


def loadClubs():
    with open(CLUB_DB_PATH) as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open(COMPETITION_DB_PATH) as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():

    for club in clubs:
        if club['email'] == request.form['email']:
            return render_template(
                'welcome.html',
                club=club,
                past_competitions=utils.get_past_competitions(competitions),
                future_competitions=utils.get_future_competitions(competitions)
            )

    return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):

    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]

    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)

    else:
        flash("Something went wrong-please try again")
        return render_template(
            'welcome.html',
            club=club,
            past_competitions=utils.get_past_competitions(competitions),
            future_competitions=utils.get_future_competitions(competitions)
        )


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():

    competition_name = request.form['competition']
    club_name = request.form['club']

    competition = [c for c in competitions if c['name'] == competition_name][0]
    club = [c for c in clubs if c['name'] == club_name][0]

    placesRequired = int(request.form['places'])
    available_points = int(club['points'])

    if placesRequired > 12:
        placesRequired = 12
        flash('You cannot book more than 12 places.')
        return render_template('booking.html', competition=competition_name, club=club_name)      
    
    elif placesRequired > available_points:
        placesRequired = available_points
        flash("You don't have enought points")
        return render_template('booking.html', competition=competition_name, club=club_name)

    else:
        flash('Great-booking complete!')

        competition['numberOfPlaces'] = str(int(competition['numberOfPlaces']) - placesRequired)
        club['points'] = str(int(club['points']) - placesRequired)

        return render_template(
            'welcome.html',
            club=club,
            past_competitions=utils.get_past_competitions(competitions),
            future_competitions=utils.get_future_competitions(competitions)
        )


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
