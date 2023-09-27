def choose_teams_menu():
    """Displays the menu of available teams and lets user pick his favorite team and returns the favorite team"""
    """
    """
    print("------ List of Currently Playing Teams ------")
    print('')
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

def main_menu(fav_team):
    """Displays menu with the stats available for the player to view"""
    print('')
    print('----- Main Menu -----')
    print(f'1. Stats of your team {fav_team}')
    print(f'2. Stats of {fav_team} against another team')
    print(f'3. Change your favorite team')
    print(f'4. Exit')

    opt = input('Enter options between 1-4: ')
    
    return int(opt)


def first_sub_menu(fav_team):
    print(f'----------- Self Analysis of your team {fav_team} --------------')
    print(f'1. Team performance (Win%, Number of matches won/lost)')
    print(f'2. MOTM Records (Man of the match records)')
    print(f'3. Playoffs record')
    print(f'4. Go back to Main Menu')

    opt = input('Enter options between 1-4: ')
    
    return int(opt)


def second_sub_menu(fav_team, teamB):
    print(f'----------- Performance Against Other Team --------------')
    print(f'1. Team Performance of {fav_team} against {teamB}')
    print(f'2. How does {fav_team} stand against {teamB} in playoffs')
    print(f'3. Change the team you would like to compare against')
    print(f'4. Go back to Main Menu')

    opt = input('Enter options between 1-4: ')

    return int(opt)