import statsapi
import re
from datetime import date, timedelta
from dateutil.tz import tzlocal
from dateutil.parser import isoparse

txt1 = input("What would you like to see: \n(1) Latest game results \n(2) Schedule information \n(3) MLB standings \n")
data_req = txt1

if data_req == "3":
    txt2 = input("Do you want the AL, NL, or both?")
    if txt2.casefold() == "al":
        print(statsapi.standings(leagueId=103))
    elif txt2.casefold() == "nl":
        print(statsapi.standings(leagueId=104))
    else:
        print(statsapi.standings(leagueId=103))
        print(statsapi.standings(leagueId=104))

else:
    txt = input("Name your team: ")
    team_name = txt
    if data_req == "1":
        def get_team_name(team_name):
	        team = statsapi.lookup_team(team_name)
	        return str(team[0]['id'])

        def recent_game():
	        team_number = get_team_name(team_name)
	        game = statsapi.last_game(team_number)
	        return game

        def show_boxscore():
	        game = recent_game()
	        box_score = statsapi.boxscore(game, battingBox=True, battingInfo=True, fieldingInfo=True, pitchingBox=True, gameInfo=True, timecode=None)
	        print(box_score)

        def show_linescore():
	        game = recent_game()
	        line_score = statsapi.linescore(game, timecode=None)
	        print(line_score)


        second_check = input("Do you want to see the latest full boxscore (1) or linescore (2)?")

        if second_check == "1":
	        show_boxscore()
        else:
	        show_linescore()

    elif data_req == "2":
        def get_team_name(team_name):
            team = statsapi.lookup_team(team_name)
            return str(team[0]['id'])
     
        def sched():
            crew = get_team_name(team_name)
            agenda = statsapi.schedule(start_date=date.today(),end_date=date.today() + timedelta(days=2),team=crew)
            for x in agenda:
                appt = x['game_datetime']
                pattern = r'Z'
                mod_appt = re.sub(pattern, '',appt)
                utc_time = isoparse(mod_appt) 
                local_time = utc_time.astimezone(tzlocal())
                local_game_time = local_time.strftime("%Y-%m-%d %H:%M")
                print(local_game_time + " - " + x['away_name'] + " @ " + x['home_name'] + " (" + x['status'] + ")")

        sched()
