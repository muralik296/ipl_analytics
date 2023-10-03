"""The data from the csv is picked up from 
https://www.kaggle.com/datasets/vora1011/ipl-2008-to-2021-all-match-dataset
"""
import sys
from map import map
from utils import get_matches_of_fav_team
from about import about_app
from menus import choose_teams_menu,main_menu,first_sub_menu,second_sub_menu
from validators import validate_change_teams,validate_team_input
from secondMenuHelpers import display_performance_against_teamB,display_playoff_record_teamA_teamB
from firstMenuHelpers import get_team_performance,playoff_record,display_teamA_performance,motm,display_motm_awardees_teamA,display_playoff_record_teamA


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
                                result = get_team_performance(fav_team,fav_team_list)
                                display_teamA_performance(fav_team,result)

                            # 1.2 is MOTM records 
                            elif (first_sub_option  == 'B'):
                                # result contains the man of the match awardees for the team
                                result = motm(fav_team,fav_team_list)

                                display_motm_awardees_teamA(result)
                                    
                            #1.3 is Playoffs record
                            elif (first_sub_option == 'C'): 
                                # result contains the list of matches where team has qualified for playoffs 
                                result = playoff_record(fav_team_list)
                                
                                #displays the playoff record between teamA vs teamB
                                display_playoff_record_teamA(result,fav_team)
                            
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
                                        display_performance_against_teamB(fav_team,fav_team_list,teamB)

                                    # 2.2 playoff record against teamB
                                    elif (second_sub_option == 'B'):
                                        display_playoff_record_teamA_teamB(fav_team,fav_team_list,teamB)
                                            
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

