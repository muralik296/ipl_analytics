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

    opt = (input('Enter options between 1-4: ')).strip()
    
    return int(opt)


def first_sub_menu(fav_team):
    print(f'----------- Self Analysis of your team {fav_team} --------------')
    print(f'a. Team performance (Win%, Number of matches won/lost)')
    print(f'b. MOTM Records (Man of the match records)')
    print(f'c. Playoffs record')
    print(f'd. Go back to Main Menu')

    opt = input('Enter options (a-d): ')
    
    return opt.upper().strip()


def second_sub_menu(fav_team, teamB):
    print(f'----------- Performance Against Other Team --------------')
    print(f'a. Team Performance of {fav_team} against {teamB}')
    print(f'b. How does {fav_team} stand against {teamB} in playoffs')
    print(f'c. Change the team you would like to compare against')
    print(f'd. Go back to Main Menu')

    opt = input('Enter options (a-d): ')

    return opt.upper().strip()