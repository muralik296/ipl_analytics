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


def display_teamA_performance(fav_team,result):
        """ Displays teamA performance in 1st submenu 1st option """
        total_matches,number_of_wins,number_of_losses,no_result,success_rate  = result
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

def display_motm_awardees_teamA(result):
        """Using the result from the motm() function, print the man of match awardee with max number of awards"""
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
            # max_no_motm => maximum number with man of the match awards
            max_no_motm = max(result, key=lambda x: x[1])[1]
            # names with maximum number of awards
            names_with_max_awards = ','.join([name for name, awards in result if awards == max_no_motm])
            
            print(f'Highest Man of the Match Awards: {names_with_max_awards}')
            print()

def display_playoff_record_teamA(result,fav_team):
        """ Displays the playoff record of fav_team """
        # this will give 5 spaces, 40 spaces to the right and so on
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

