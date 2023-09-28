import sys
from map import map
from utils import get_matches_of_fav_team
from about import about_app
from menus import choose_teams_menu,main_menu,first_sub_menu,second_sub_menu

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


def motm(teamA,teamAList,year1,year2):
    """ Returns an object containing the name of player and number of times they have won man of the match awards between year 1 and year 2 """
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

def validate_team_input(team):
    if (team not in map.keys()):
        print(f'Invalid input, please select from the list of available teams {list(map.keys())}')
        return False
    return True

def validate_change_teams(fav_team,teamB):
    if(fav_team == teamB):
        print('The opposing team and your current team cannot be the same!')
        return False
    return True


def infer_performance(success_rate,teamA,year1,year2):
    if (success_rate < 50):
        if (year1 == year2):
            print(f'{teamA} performance has been below par in the year {year1}')
        else:
            print(f'{teamA} performance has been below par between the years {year1} and {year2}')

    else:
        if (year1 == year2):
            print(f'{teamA} performance has been above par in the year {year1}')
        else:
            print(f'{teamA} performance has been above par between the years {year1} and {year2}')


def input_years():
    print('-- Input the seasons range --')
    year1 = (input('Enter first year: ')).strip()
    year2 = (input('Enter second year: ')).strip()
    return year1,year2

def main():
    try:
        # about the app
        about_app()

        while (True):

            # print the teams available
            choose_teams_menu()

            fav_team = (input('Enter the team you would like to view stats : ')).upper()

            if (validate_team_input(fav_team)):
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
                            
                            if (first_sub_option == 'A'):
                                # stats between which seasons
                                year1,year2=input_years()
                                
                                if((year1.isnumeric() == False) or (year2.isnumeric() == False)):
                                    print('Invalid years input, please enter values between 2008 and 2022')

                                elif(int(year1) < 2008 or int(year2) > 2022):
                                    print('Invalid years input, please enter values between 2008 and 2022')

                                else:
                                    year1=int(year1)
                                    year2=int(year2)
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
                                        success_rate = round((number_of_wins/total_matches_played)*100)
                                        print(f'Win Percentage: {success_rate} %')
                                        infer_performance(success_rate,fav_team,year1,year2)
                                        print('')

                            # 1.2 is MOTM records 
                            elif (first_sub_option  == 'B'):

                                # stats between which seasons
                                year1,year2 = input_years()
                                if((year1.isnumeric() == False) or (year2.isnumeric() == False)):
                                    print('Invalid years input, please enter values between 2008 and 2022')
   
                                elif(int(year1) < 2008 or int(year2) > 2022):
                                    print('Invalid years input, please enter values between 2008 and 2022')
                                else:
                                    year1=int(year1)
                                    year2=int(year2)
                                    result = motm(fav_team,fav_team_list,year1,year2)
                                    
                                    # Print the table
                                    print()
                                    print(f'The Man of the Match Awardees between {year1} and {year2}')
                                    print("{:<20} {:<5}".format("Player", "Number of MOTM"))
                                    print("-" * 30)
                                    for player, count in result:
                                        print("{:<20} {:<5}".format(player, count))
                                    #inference
                                    if (len(result) == 0):
                                        print('Team has not played during those seasons')
                                    else:
                                        print(f'{result[0][0]} is the player with most number of awards')
                                        print('')

                            #1.3 is Playoffs record
                            elif (first_sub_option == 'C'):
                                
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
                                
                                # print only if any wins in the years
                                conditional_string = f"{fav_team} has won {number_of_wins} IPL Cups in the years {string_with_years}." if (number_of_wins>0) else f"{fav_team} has not won any IPL Cups" 
                                
                                print(f'{conditional_string}')
                            
                            #1.4 Takes user back to main menu
                            elif (first_sub_option == 'D'):
                                break
                    
                    elif (opt == 2):
                        # the second sub menu
                        teamB = (input('Enter the opponent: ')).upper()

                        if (validate_team_input(teamB)):
                            #validating changing of opposing team
                            if (validate_change_teams(fav_team,map[teamB])):

                                #normalize input data
                                teamB = map[teamB]

                                while (True):
                                    print()
                                    #second sub menu
                                    second_sub_option = second_sub_menu(fav_team, teamB)

                                    # 2.1 performance against other team
                                    if (second_sub_option == 'A'):
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
                                    elif (second_sub_option == 'B'):
                                        # playoff record
                                        print(f'-------- PLAYOFF RECORD ({fav_team}) v ({teamB}) ----------')
                                        print()
                                        print("{:<5} {:<20} {:<40} {:<40} {:<40} {:<40}".format("Year", "Playoff Match","First Team","Second Team","Winning Team","Venue"))
                                        print("-" * 185)
                                        
                                        teamA_cup = 0
                                        teamA_playoffs = 0

                                        teamB_playoffs = 0
                                        teamB_cup = 0

                                        both_playoffs = 0
                                        
                                        teamAB_wins  = 0
                                        teamAB_losses = 0
                                        for ele in fav_team_list:
                                            # filtering items where teamB and teamA have played and also its a qualifier match(playoff)
                                            if ((ele[5] == teamB or ele[6] == teamB) and (ele[4] == 'Qualifier' or ele[4] == 'Final')):
                                                both_playoffs+=1
                                                if(ele[11] == fav_team):
                                                    teamAB_wins+=1
                                                else:
                                                    teamAB_losses+=1
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

                                            
                                        print()

                                        print(f'{fav_team} and {teamB} went head-to-head in {both_playoffs} playoff matches')
                                        print(f'{fav_team} has won {teamA_cup} IPL tournaments across all seasons')
                                        print(f'{teamB} has won {teamB_cup} IPL tournaments across all seasons')
                                        print('')
                                        print(f'{fav_team} has played {teamA_playoffs} playoff matches')
                                        print(f'{teamB} has played {teamB_playoffs} playoff matches')
                                        
                                        more_playoff = f"{teamB} has played more playoff games than {fav_team}" if (teamB_playoffs>teamA_playoffs) else f"{fav_team} has played more playoff games than {teamB}" 

                                        print(more_playoff)
                                        # more_head_head_playoffs = f"{teamB} performed better in playoffs against {fav_team}" if (teamAB_losses>teamAB_wins) else f"{fav_team} performed better in playoffs  against {teamB}"
                                        # print(more_head_head_playoffs)
                                            
                                    # switch to another teamB
                                    elif (second_sub_option == 'C'):
                                        print("--- Change your opposing team ---")
                                        choose_teams_menu()
                                        alternative_opt = (input('Enter the opposing team: ')).upper()

                                        if (validate_team_input(alternative_opt)):
                                            #validating changing of opposing team
                                            if (validate_change_teams(fav_team,map[alternative_opt])):
                                                teamB = map[alternative_opt]

                                    elif(second_sub_option == 'D'):
                                        break
                                    
                                    else:
                                        print('Invalid option. Please choose between 1-4')

                    elif (opt == 3):
                        print('----- Change your primary team --------')
                        choose_teams_menu()
                        alternative_opt = (input('Enter the team you would like to change to :')).upper()

                        if (validate_team_input(alternative_opt)):
                            fav_team = map[alternative_opt]
                            fav_team_list = get_matches_of_fav_team(fav_team)

                    elif (opt == 4):
                        # break
                        sys.exit(0)
                    else:
                        print('Invalid Option, please select options between 1-3')
            
    except ZeroDivisionError:
        print('Err: Encountered division by zero')
    except ValueError:
        print('Err: Invalid Input')
    
    finally:
        print('Thank you for using our application')

main()

