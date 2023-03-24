from team_model import Team
from random import randint

def get_match_result(Team1, Team2):
    T1_goals = round(Team1.attack / Team2.defense) + randint(0, round(Team1.midfield/30))
    T2_goals = round(Team2.attack / Team1.defense) + randint(0, round(Team2.midfield/30))
    return f"{Team1.name} {T1_goals} {T2_goals} {Team2.name}"

team1 = Team("Spurs", 9, 60, 40)
team2 = Team("Sheffield Wednesday", 98, 25, 50)

print(get_match_result(team1, team2))