#csv
import csv

def get_matches_of_fav_team(fav_team):
    # below will contain the filtered list only where the favorite team is either teamA or teamB
    fav_team_list = []
    with open('matches.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
        #5th and 6th indice indicates the teams playing teamA v teamB
            if (row[5] == fav_team or row[6] == fav_team):
                # create a list with the favorite teams playing
                fav_team_list.append(row)
    return fav_team_list