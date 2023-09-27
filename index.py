from map import map
from utils import get_matches_of_fav_team
from about import about_app
import pdb; 


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


def view_win_loss_stats_fav_team(teamA,teamAList,year1,year2):
        """Returns a tuple with no. of wins, losses and no result matches of teamA between year1 and year2"""
        number_of_wins = 0
        number_of_losses = 0
        no_result = 0

        for ele in teamAList:
            # if year is empty it means all years / if year is not empty but equal to a certain season
            # ele[3] indicates the year when the match was played
            if (int(ele[3]) >= year1 and int(ele[3]) <= year2):
                # 11th column in the csv indicates the winning team
                if(ele[11] == teamA):
                    number_of_wins+=1
                elif (ele[11] == 'NA'):
                    no_result+=1
                else:
                    number_of_losses+=1
        return (number_of_wins,number_of_losses,no_result)



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

    opt = input('Enter options between 1-3: ')

    return int(opt)

def motm(teamA,teamAList,year1,year2):

    # stores the number of man of the match awardees
    motm = {}

    #ele[15] => indicates man of the match awardee
    for ele in teamAList:

        # making sure that it is in between those two year ranges and ele[11] indicates the winnning team
        if (int(ele[3]) >= year1 and int(ele[3]) <= year2):
            
            '''Here we need to check if the Man of the match is actually a player in teamA and not part of teamB , so we ensure we check 
                that the player's name belongs in the teamA array

                Why? because in some cases,even though the winning side is teamA the MOTM can be of teamB
            '''

            if (ele[5] == teamA and ele[15] in eval(ele[16]) or (ele[6] == teamA and ele[15] in eval(ele[17]))):
                if (ele[15] in motm):
                    motm[ele[15]]+=1
                else:
                    motm[ele[15]] = 1

    # sorting the dictonary by who won the most number of motm awards                
    sorted_motm = sorted(motm.items(), key=lambda x:x[1], reverse=True)

    return sorted_motm

def playoff_record(teamAList):
    qualifiers = []
    for ele in teamAList:
        if (ele[4] == 'Qualifier' or ele[4] == 'Final'):
            qualifiers.append((ele))
    return qualifiers

def main():
    try:
        # about the app
        about_app()

        while (True):

            # print the teams available
            choose_teams_menu()

            fav_team = input('Enter the team you would like to view stats : ')

            # if user enters invalid team or unsupported
            if (fav_team not in map.keys()):
                print(f'Invalid input, please select from the list of available teams {map.keys()}')

            else:
                fav_team = map[fav_team]

                fav_team_list = get_matches_of_fav_team(fav_team)

                while (True):
                    # main menu with the main 3 options
                    opt = int(main_menu(fav_team))
                    
                    print('')

                    # option 1 is to check for the wins/losses stats of teamA
                    if (opt == 1):
                        
                        # the first sub menu
                        
                        while(True):
                            print()
                            # first sub menu
                            first_sub_option = first_sub_menu(fav_team)      
                            
                            
                            # 1.1 is performance between two years
                            if (first_sub_option == 1):
                                # stats between which seasons
                                year1 = int(input('Enter first year: '))
                                year2 = int(input('Enter second year: '))

                                #? TO DO year1 and year2 validation to be done            

                                number_of_wins,number_of_losses,no_result = view_win_loss_stats_fav_team(fav_team,fav_team_list,year1,year2)
                                total_matches_played = (number_of_wins+number_of_losses+no_result)
                                
                                if (total_matches_played == 0):
                                    print('The team did not play during those seasons')
                                else:
                                    print('')
                                    print(f'------ Team performance between {year1} and {year2} ------')
                                    print(f'Number of wins:\t{number_of_wins}')
                                    print(f'Lost Matches:\t{number_of_losses}')
                                    print(f'No result :\t{no_result}')
                                    print('')
                                    print(f'Total Matches Played: \t{total_matches_played}')
                                    print(f'Win Percentage\t{round((number_of_wins/total_matches_played)*100)} %')
                                    print('')

                            # 1.2 is MOTM records 
                            elif (first_sub_option  == 2):

                                # stats between which seasons
                                year1 = int(input('Enter years between: '))
                                year2 = int(input('Enter second year: '))

                                result = motm(fav_team,fav_team_list,year1,year2)

                                # Print the table
                                print()
                                print(f'The Man of the Match Awardees between {year1} and {year2}')
                                print("{:<20} {:<5}".format("Player", "Number of MOTM"))
                                print("-" * 30)

                                for player, count in result:
                                    print("{:<20} {:<5}".format(player, count))

                            #1.3 is Playoffs record
                            elif (first_sub_option == 3):
                                
                                result = playoff_record(fav_team_list)
                                print("{:<5} {:<20} {:<40} {:<40} {:<40} {:<40}".format("Year", "Playoff Match","First Team","Second Team","Winning Team","Venue"))
                                print("-" * 185)
                                number_of_wins = 0
                                years_won = []
                                for ele in result:
                                    # finding out how many times a favorite team has won the final
                                    if (ele[11] == fav_team and ele[4] == 'Final'):
                                        number_of_wins+=1
                                        years_won.append(ele[3])
                                    print("{:<5} {:<20} {:<40} {:<40} {:<40} {:<40}".format(ele[3], ele[4], ele[5], ele[6],ele[11],ele[7]))
                                string_with_years = ','.join(years_won)
                                print('')
                                print(f'{fav_team} has won {number_of_wins} tournaments in the years {string_with_years}')
                            
                            #1.4 Takes user back to main menu
                            elif (first_sub_option == 4):
                                break
                    
                    elif (opt == 2):
                        # the second sub menu
                        teamB = input('Enter the team against which you would like to view stats: ')
                        #normalize input data
                        teamB =map[teamB]

                        while (True):
                            print()

                            #second sub menu
                            second_sub_option = second_sub_menu(fav_team, teamB)

                            # 2.1 performance against other team
                            if (second_sub_option == 1):
                                toss_wins = 0
                                head_head_playoffs = 0
                                playoff_wins = 0
                                number_of_wins = 0
                                number_of_losses = 0

                                print("{:<5} {:<30} {:<30} {:<30} {:<30} {:<30}".format("Year","First Team","Second Team","Toss winner","Winning Team","Venue"))
                                print("-" * 165)
                                for ele in fav_team_list:
                                    if (ele[5] == teamB or ele[6] == teamB):
                                        
                                        print("{:<5} {:<30} {:<30} {:<30} {:<30} {:<30}".format(ele[3], ele[5],ele[6],ele[8],ele[11],ele[7]))
                                        
                                        if (ele[11] == fav_team):
                                            number_of_wins+=1
                                        
                                        if (ele[11] == teamB):
                                            number_of_losses+=1
                                        
                                        if (ele[8] == fav_team):
                                            toss_wins+=1

                                        if (ele[4] == 'Qualifier' or ele[4] == 'Final'):
                                            head_head_playoffs+=1
                                            if (ele[11] == teamB):
                                                playoff_wins+=1
                                print("")
                                total_matches = number_of_wins + number_of_losses

                                if(total_matches != 0):                     
                                    print(f'{fav_team} has played {total_matches} matches against {teamB}')
                                    print(f'{fav_team} has won {number_of_wins} head-to-head contests against {teamB}')

                                    print(f'Win % of {fav_team} against {teamB}: \t{round((number_of_wins/total_matches)*100)}%')
                                    print(f'Win % tosses of {fav_team} against {teamB}: \t{round((toss_wins/total_matches*100))}%')
                                else:
                                    print(f'No games played between {fav_team} and {teamB}')

                            # playoff record of both the teams
                            elif (second_sub_option == 2):
                                # playoff record
                                print("{:<5} {:<20} {:<40} {:<40} {:<40} {:<40}".format("Year", "Playoff Match","First Team","Second Team","Winning Team","Venue"))
                                print("-" * 185)
                                
                                teamA_cup = 0
                                teamA_playoffs = 0

                                teamB_playoffs = 0
                                teamB_cup = 0

                                both_playoffs = 0

                                for ele in fav_team_list:
                                    # filtering items where teamB and teamA have played and also its a qualifier match(playoff)
                                    if ((ele[5] == teamB or ele[6] == teamB) and (ele[4] == 'Qualifier' or ele[4] == 'Final')):
                                        both_playoffs+=1

                                        print("{:<5} {:<20} {:<40} {:<40} {:<40} {:<40}".format(ele[3], ele[4], ele[5], ele[6],ele[11],ele[7]))
                                    
                                    if ((ele[4] == 'Qualifier' or ele[4] == 'Final')):
                                        teamA_playoffs+=1
                                        if (ele[11] == fav_team and ele[4] == 'Final'):
                                            teamA_cup+=1
                                
                                teamBResults = get_matches_of_fav_team(teamB)

                                for ele in teamBResults:                                                     
                                    if ((ele[4] == 'Qualifier' or ele[4] == 'Final')):
                                        teamB_playoffs+=1
                                        if (ele[11] == teamB and ele[4] == 'Final'):
                                            teamB_cup+=1

                                    
                                print("")

                                print(f'{fav_team} and {teamB} went head-to-head in {both_playoffs} playoff matches')
                                print(f'{fav_team} has won {teamA_cup} IPL tournaments')
                                print(f'{teamB} has won {teamB_cup} IPL tournaments')
                                print('')
                                print(f'{fav_team} has played {teamA_playoffs} playoff matches')
                                print(f'{teamB} has played {teamB_playoffs} playoff matches')
                                    
                            # switch to another teamB
                            elif (second_sub_option == 3):
                                print("--- Switch teamB ---")
                                print("Select the opposing team you'd prefer to use for comparison")
                                choose_teams_menu()
                                teamB = input('Enter the opposing team: ')
                                teamB = map[teamB]
                                
                            elif(second_sub_option == 4):
                                break
                            
                            else:
                                print('Invalid option. Please choose between 1-4')

                    elif (opt == 3):
                        print('----- Change your primary team --------')
                        choose_teams_menu()
                        fav_team = input('Enter the team you would like to change to :')
                        # if user enters invalid team or unsupported
                        if (fav_team not in map.keys()):
                            print(f'Invalid input, please select from the list of available teams {map.keys()}')

                        fav_team = map[fav_team]
                        fav_team_list = get_matches_of_fav_team(fav_team)

                    elif (opt == 4):
                        exit()

                    else:
                        print('Invalid Option, please select options between 1-3')
            
    except ZeroDivisionError:
        print('Err: Encountered division by zero')
    
    finally:
        print('Thank you for using our application')

main()

