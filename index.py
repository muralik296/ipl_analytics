from map import map
from utils import get_matches_of_fav_team
from about import about_app


def choose_teams_menu():
    """Displays the menu of available teams and lets user pick his favorite team and returns the favorite team"""
    """
    """
    print('1. Gujarat Titans (GT)')
    print('2. Chennai Super Kings (CSK)')
    print('3. Lucknow Super Giants (LSG)')
    print('4. Mumbai Indians (MI)')
    print('5. Rajasthan Royals (RR)')
    print('6. Royal Challengers Banglore (RCB)')
    print('7. Kolkata Knight Riders (KKR)')
    print('8. Punjab Kings (PKS)')
    print('9. Delhi Capitals (DC)')
    print('10. Sunrisers Hyderabad (SRH)')
    print('')
    option = input('Enter Your Preffered Team: ')
    return map[option]


def view_win_loss_stats_fav_team(teamA,teamAList,year):
        """Returns a tuple with no. of wins, losses and no result matches of teamA"""
        number_of_wins = 0
        number_of_losses = 0
        no_result = 0
        
        # ele[3] => year

        for ele in teamAList:
            # if year is empty it means all years / if year is not empty but equal to a certain season
            if (year == '' or year == ele[3]):
                # 11th column in the csv indicates the winning team
                if(ele[11] == teamA):
                    number_of_wins+=1
                elif (ele[11] == 'NA'):
                    no_result+=1
                else:
                    number_of_losses+=1
        return (number_of_wins,number_of_losses,no_result)


def view_win_loss_stats_against_teamB(teamA,teamB,teamAList,year):
    """Returns a tuple with no. of wins, losses and no result matches of teamA against teamB"""
    number_of_wins = 0
    number_of_losses=0
    no_result=0
    for ele in teamAList:
        # if year is empty it means all years / if year is not empty but equal to a certain season
        if (year == '' or year == ele[3]):
            if (ele[5] == teamB or ele[6] == teamB):
                # 11th column in the csv indicates the winning team
                if(ele[11] == teamA):
                    number_of_wins+=1
                elif (ele[11] == 'NA'):
                    no_result+=1
                else:
                    number_of_losses+=1
    return (number_of_wins,number_of_losses,no_result)

def choose_menu(fav_team):
    """Displays menu with the stats available for the player to view"""
    
    print('---------- Stats 🏏 ----------')
    print(f'1. View win/loss stats of {fav_team}')
    print(f'2. View win/loss stats against another team')
    print(f'3. Display Playoff record of {fav_team}')
    print(f'4. Exit')

    opt = input('Enter options between 1-3: ')
    return opt


about_app()


def main():
    try:
        game_over = True

        while (game_over):

            #fav_team is the team the user would like to view the stats for
            fav_team = choose_teams_menu()

            # this will contain all the information pertaining to your fav team (teamA)
            fav_team_list = get_matches_of_fav_team(fav_team)

            # now that we have the filtered list=>fav_team_list with only our favorite team playing we can perform operations on it        
            go_back = True

            # if year not selected, all seasons
            year = input('Enter the season you would like to view the stats for (2008-2022), if not selected default all seasons: ')
            
            if (int(year) < 2008 or int(year) > 2022):
                print('Invalid season. Please enter seasons between 2008-2022')
                break
            
            # ? TO DO Validate year if empty


            while (go_back):
                opt = int(choose_menu(fav_team))
                print('')

                # option 1 is to check for the wins/losses stats of teamA
                if (opt == 1):
                    number_of_wins,number_of_losses,no_result = view_win_loss_stats_fav_team(fav_team,fav_team_list,year)
                    print(f'Number of wins: {number_of_wins}')
                    print(f'Number of losses: {number_of_losses}')
                    print(f'No result: {no_result}')
                    
                    total_matches = (number_of_wins+number_of_losses+no_result)

                    if (total_matches == 0):
                        print(f'The team did not play in {year}')
                        break

                    winPercentage = round(number_of_wins/(number_of_wins+number_of_losses+no_result)*100,2)
                    print(f'Win Percentage : {winPercentage}%')
                
                # option 2 is to view wins/losses against another team
                elif (opt == 2):
                    teamB =  choose_teams_menu()
                    number_of_wins,number_of_losses,no_result = view_win_loss_stats_against_teamB(fav_team,teamB,fav_team_list,year)
                    
                    print(f'Number of wins: {number_of_wins}')
                    print(f'Number of losses: {number_of_losses}')
                    print(f'No result: {no_result}')

                    print(f'Win Percentage : {round((number_of_wins/(number_of_wins+number_of_losses+no_result))*100),2}%')

                # option 3 is to view playoff record of your current team and standings of other teams
                elif (opt == 3):
                    pass
                
                else:
                    exit()
                # go_back = input('Go Back to Main Menu: ')
            
            #game_over = input('Would you like to choose another team to view their stats: ')

    except ZeroDivisionError:
        print('Err: Encountered division by zero')
    
    finally:
        print('Thank you for choosing our application')

main()