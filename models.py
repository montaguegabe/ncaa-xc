"""
models.py

Use this file to define classes that encapsulate running, meet, and ranking logic that is
independent of scraping or user-interaction logic.
"""

from datetime import *


class Athlete(object):
    def __init__(self, name, team=None):
        super(Athlete, self).__init__()
        self.name = name
        self.team = team


class Team(object):
    def __init__(self, name, region):
        super(Team, self).__init__()
        self.name = name
        self.athletes = []
        self.region = region

    def add(athlete):
        self.athletes.append(athlete)


class Meet(object):
    
    def __init__(self):
        super(Meet, self).__init__()

        self.date = date.today()
        self.finishers = []

    def get_teams():
        team_set = set()
        for finisher in self.finishers:
            team_set.add(finisher.team)

    # Return a list of the top teams
    def score_teams():

        team_scores = {}
        team_finishers_count = {}
        place = 1

        for finisher in self.finishers:
            team = finisher.team

            # Ignore runners who are after the team's top 7
            if team_finishers_count.get(team, default=0) > 7: continue

            team_scores[team] = team_scores.get(team, default=0) + place

            team_finishers_count[team] = team_finishers_count.get(team, default=0) + 1
            place += 1

        team_score_list = team_scores.items()
        team_score_list.sort(key=lambda pair: pair[1])

        return team_score_list


