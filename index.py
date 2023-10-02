"""The data from the csv is picked up from 
https://www.kaggle.com/datasets/vora1011/ipl-2008-to-2021-all-match-dataset
"""
import sys
from map import map
from utils import get_matches_of_fav_team
from about import about_app
from menus import choose_teams_menu,main_menu,first_sub_menu,second_sub_menu
from validators import validate_change_teams,validate_team_input

def get_team_performance(teamA,teamAList):
        """Returns a tuple with no. of wins, losses and no result matches of teamA"""
        number_of_wins = 0
        number_of_losses = 0
        no_result = 0

        for ele in teamAList:
        # if year is empty it means all years / if year is not empty but equal to a certain season
        # ele[3] indicates the year when the match was played
            # 11th column in the csv indicates the winning team
            if(ele[11] == teamA):
                number_of_wins+=1
            elif (ele[11] == 'NA'):
                no_result+=1
            else:
                number_of_losses+=1
        total_matches = (number_of_wins+number_of_losses+no_result)
        success_rate = round((number_of_wins/(number_of_wins+number_of_losses))*100,1)
        return (total_matches,number_of_wins,number_of_losses,no_result,success_rate)

def motm(teamA,teamAList):
    """ Returns an object containing the name of player and number of times they have won man of the match awards between year 1 and year 2 """
    # stores the number of man of the match awardees
    motm = {}

    for ele in teamAList:

        # making sure that it is in between those two year ranges and ele[11] indicates the winnning team
        #ele 16 is a list but when read its a string, usage of eval() => list
        if (ele[5] == teamA and ele[15] in eval(ele[16]) or (ele[6] == teamA and ele[15] in eval(ele[17]))):
            if (ele[15] in motm):
                motm[ele[15]]+=1
            else:
                motm[ele[15]] = 1

    # sorting the dictonary by who won the most number of motm awards                
    sorted_motm = sorted(motm.items(), key=lambda x:x[1], reverse=True)

    return sorted_motm

def playoff_record(teamAList):
    """Returns the playoff matches played by teamA which includes qualifiers and finals"""
    qualifiers = []
    for ele in teamAList:
        if (ele[4] == 'Qualifier' or ele[4] == 'Final'):
            qualifiers.append((ele))
    return qualifiers

def infer_performance(success_rate,teamA):
    """Prints the team performance based on the succes_rate, if success_rate is greater than 50% considering it as above par"""
    if (success_rate < 50):
        print(f'{teamA} performance has been below par')

    else:
        print(f'{teamA} performance has been above par')


def main():
    """ Main function """
    try:
        # about the app
        about_app()

        while (True):

            # print the teams available
            choose_teams_menu()

            fav_team = (input('Enter the team you would like to view stats: ')).upper()

            if (validate_team_input(fav_team)):
                fav_team = map[fav_team]

                fav_team_list = get_matches_of_fav_team(fav_team)

                while (True):
                    # main menu with the main 3 options
                    opt = int(main_menu(fav_team))
                    print()
                    # option 1 is to check for the wins/losses stats of teamA
                    if (opt == 1):
                        
                        # the first sub menu
                        
                        while(True):
                            print()
                            # first sub menu
                            first_sub_option = first_sub_menu(fav_team)

                            # team performance in the year range
                            if (first_sub_option == 'A'):

                                total_matches,number_of_wins,number_of_losses,no_result,success_rate = get_team_performance(fav_team,fav_team_list)

                                if (total_matches == 0):
                                    print('The team did not play during those seasons')
                                else:
                                    print('')
                                    print(f'Team performance of {fav_team}')
                                    print(f'Total Matches Played : {total_matches}')
                                    print(f'Won Matches : {number_of_wins}')
                                    print(f'Lost Matches: {number_of_losses}')
                                    print(f'No result : {no_result}')
                                    print(f'Overall success rate of {fav_team} : {success_rate} %')
                                    infer_performance(success_rate,fav_team)
                                    print()

                            # 1.2 is MOTM records 
                            elif (first_sub_option  == 'B'):
                                # result contains the man of the match awardees for the team
                                result = motm(fav_team,fav_team_list)
                                
                                # Print the table
                                print()
                                print(f'The Man of the Match Awardees across all seasons')
                                print("{:<20} {:<5}".format("Player", "Number of MOTM"))
                                print("-" * 30)
                                for player, count in result:
                                    print("{:<20} {:<5}".format(player, count))

                                #inference
                                if (len(result) == 0):
                                    print('Team has not played during those seasons')
                                else:
                                    #[0][0] indicates the player with maximum number of man of the match awards
                                    print(f'{result[0][0]} is the player with most number of awards')
                                    print('')

                            #1.3 is Playoffs record
                            elif (first_sub_option == 'C'): 
                                # result contains the list of matches where team has qualified for playoffs 
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
                                
                                # conditional string if team has won any cup
                                conditional_string = f"{fav_team} has won {number_of_wins} IPL Cups in the years {string_with_years}." if (number_of_wins>0) else f"{fav_team} has not won any IPL Cups" 
                                
                                print(f'{conditional_string}')
                            
                            #1.4 Takes user back to main menu
                            elif (first_sub_option == 'D'):
                                break
                    # 2
                    elif (opt == 2):
                        choose_teams_menu()
                        teamB = (input('Enter the opponent: ')).upper()

                        # TODO validate the input at once

                        if (validate_team_input(teamB) and validate_change_teams(fav_team,map[teamB])):
                                
                                #normalize teamB to the specified team name
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

                                            print(f'Success rate of {fav_team} against {teamB}: {round((number_of_wins/total_matches)*100)}%')
                                            print(f'Success rate of tosses of {fav_team} against {teamB}: {round((toss_wins/total_matches*100))}%')
                                        else:
                                            print(f'No games played between {fav_team} and {teamB}')

                                    # 2.2 playoff record against teamB
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
                                        print()
                                        print(f'{fav_team} has played {teamA_playoffs} playoff matches')
                                        print(f'{teamB} has played {teamB_playoffs} playoff matches')
                                        
                                        #printing the right inference
                                        if (teamB_playoffs > teamA_playoffs):
                                            print(f'{teamB} has played more playoff games than {fav_team}')
                                        elif (teamB_playoffs < teamA_playoffs):
                                            print(f'{fav_team} has played more playoff games than {teamB}')
                                        else:
                                            print(f'{fav_team} and {teamB} have played same number of playoff games')
                                            
                                    # 2.3 Change teamB
                                    elif (second_sub_option == 'C'):
                                        print("--- Change your opposing team ---")
                                        choose_teams_menu()
                                        alternative_opt = (input('Enter the opposing team: ')).upper()
                                        if (validate_team_input(alternative_opt) and validate_change_teams(fav_team,map[alternative_opt])):                   
                                            teamB = map[alternative_opt]
                                    # 2.4 go back to main menu
                                    elif(second_sub_option == 'D'):
                                        break
                                    
                                    else:
                                        pass

                    elif (opt == 3):
                        print('----- Change your primary team --------')
                        choose_teams_menu()
                        alternative_opt = (input('Enter the team you would like to change to :')).upper()

                        if (validate_team_input(alternative_opt)):
                            fav_team = map[alternative_opt]
                            fav_team_list = get_matches_of_fav_team(fav_team)

                    elif (opt == 4):
                        sys.exit(0)
                    else:
                        pass
                        # print('Invalid Option, please select options between 1-3')
    except FileNotFoundError:
        print('Err: Please make sure the file matches.csv is present before running the application')
        print()
    except Exception as e:
        print(e)
        print('An exception has occured')
    finally:
        print('Thank you for using our application')

main()

