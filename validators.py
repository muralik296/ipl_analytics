from map import map
from customErrorClass import InvalidInput


def validate_team_input(teamA):
    if (teamA not in map.keys()):
        raise InvalidInput(f'Invalid input, please select from the list of available teams {list(map.keys())}')
    return True

def validate_change_teams(teamA,teamB):
    try:
        if (teamA == teamB):
            raise InvalidInput(f'The opposing team and your current team cannot be the same! Please choose a team other than {teamA}')
        return True
    except InvalidInput as e:
        print(e)
        return False