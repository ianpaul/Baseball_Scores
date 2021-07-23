import statsapi
from datetime import date

txt = input("Do you want the AL, NL, or both?")

if txt.casefold() == "al":
	print(statsapi.standings(leagueId=103))
elif txt.casefold() == "nl":
	print(statsapi.standings(leagueId=104))
else:
	print(statsapi.standings(leagueId=103))
	print(statsapi.standings(leagueId=104))

