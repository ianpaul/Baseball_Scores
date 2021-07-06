import statsapi

txt = input("Name your team: ")
team_name = txt

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


second_check = input("Do you want to see the latest full boxscore (1) or linescore(2)?")

if second_check == "1":
	show_boxscore()
else:
	show_linescore()



