import statsapi
from datetime import date, timedelta

txt = input("Name your team: ")
team_name = txt

def get_team_name(team_name):
	team = statsapi.lookup_team(team_name)
	return str(team[0]['id'])

def sched():
	crew = get_team_name(team_name)
	agenda = statsapi.schedule(start_date=date.today(),end_date=date.today() + timedelta(days=2),team=crew)
	for x in agenda:
		print(x['summary'])

sched()


