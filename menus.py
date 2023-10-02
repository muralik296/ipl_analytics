from customErrorClass import InvalidInput

def choose_teams_menu():
    """Displays the menu of available teams and lets user pick his favorite team and returns the favorite team"""
    """
    """
    print("List of Currently Playing Teams")
    print('-'*45)
    print('Gujarat Titans (GT)')
    print('Chennai Super Kings (CSK)')
    print('Lucknow Super Giants (LSG)')
    print('Mumbai Indians (MI)')
    print('Rajasthan Royals (RR)')
    print('Royal Challengers Banglore (RCB)')
    print('Kolkata Knight Riders (KKR)')
    print('Punjab Kings (PKS)')
    print('Delhi Capitals (DC)')
    print('Sunrisers Hyderabad (SRH)')
    print('')
    print('Please choose the team by entering the abbrevation of the team name. e.g. to select Sunrisers Hyderabad, type "SRH" ')

def main_menu(fav_team):
    """Displays menu with the stats available for the player to view"""
    try:

        print()
        print('----- Main Menu -----')
        print(f'1. Performance of {fav_team}')
        print(f'2. Performance of {fav_team} against an opponent team')
        print(f'3. Change your favorite team')
        print(f'4. Exit')
        print()
        opt = (input('Enter options between 1-4: ')).strip()
        if (opt not in ['1','2','3','4']):
            raise InvalidInput('Invalid input, please enter options between 1-4')
        return opt
    except InvalidInput as e:
        print(e)
        return False



def first_sub_menu(fav_team):
    """Displays the first submenu when user selects Stats of their team"""
    try:
        print(f'----------- Menu Options for team analysis of {fav_team} --------------')
        print(f'a. Team performance')
        print(f'b. MOTM Records (Man of the match records)')
        print(f'c. Playoffs record')
        print(f'd. Go back to Main Menu')
        print()
        opt = input('Enter options (a-d): ')
        if (opt not in ['a','b','c','d','A','B','C','D']):
                raise InvalidInput('Invalid input, please enter options between a-d (or) A-D')
        return opt.upper().strip()
    
    except InvalidInput as e:
        print(e)
        return False 



def second_sub_menu(fav_team, teamB):
    try:

        print(f'----------- Menu options for {fav_team} vs. {teamB} --------------')
        print(f'a. Team Performance of {fav_team} against {teamB}')
        print(f'b. Performance of {fav_team} against {teamB} in playoffs')
        print(f'c. Change the team you would like to compare against')
        print(f'd. Go back to Main Menu')
        print()
        opt = input('Enter options (a-d): ')
        if (opt not in ['a','b','c','d','A','B','C','D']):
                raise InvalidInput('Invalid input, please enter options between a-d (or) A-D')
        return opt.upper().strip()
    
    except InvalidInput as e:
        print(e)
        return False 