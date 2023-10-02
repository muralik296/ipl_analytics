from map import map
from customErrorClass import InvalidInput


def validate_team_input(teamA):
    """ Validates the input given by user if exists within the allowed teams from map, returns true if all okay, else false """
    try:
        if (teamA not in map.keys()):
            raise InvalidInput(f'Invalid input, please select from the list of available teams {list(map.keys())}')
        return True
    except InvalidInput as e:
        print(e)
        return False

def validate_change_teams(teamA,teamB):
    """ Validates when user wants to change teams, makes sure teamA not equal to teamB """
    try:
        if (teamA == teamB):
            raise InvalidInput(f'The opposing team and your current team cannot be the same! Please choose a team other than {teamA}')
        return True
    except InvalidInput as e:
        print(e)
        return False