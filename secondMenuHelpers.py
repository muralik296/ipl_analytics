from utils import get_matches_of_fav_team

def display_playoff_record_teamA_teamB(fav_team,fav_team_list,teamB):
        """Displays the playoff record between team A and team B"""
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


def display_performance_against_teamB(fav_team,fav_team_list,teamB):
        """Displays performance of teamAvsteamB"""
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

        