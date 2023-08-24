match_data = [
    {"Team A": "India", "Team B": "SriLanka", "Location": "Mumbai", "Timing": "DAY"},
    {"Team A": "England", "Team B": "Australia", "Location": "Delhi", "Timing": "DAY_NIGHT"},
    {"Team A": "India", "Team B": "SouthAfrica", "Location": "Chennai", "Timing": "DAY"},
    {"Team A": "England", "Team B": "SriLanka", "Location": "Indore", "Timing": "DAY-NIGHT"},
    {"Team A": "Australia", "Team B": "SouthAfrica", "Location": "Mohali", "Timing": "DAY-NIGHT"},
    {"Team A": "India", "Team B": "Australia", "Location": "Delhi", "Timing": "DAY"}]


def list_matches_by_teama(team_name):
    for match in match_data:
        if match["Team A"] == team_name:
            print(match)
def list_matches_by_teamb(team_name):
    for match in match_data:
        if match["Team B"] == team_name:
            print(match)

def list_matches_by_location(location):
    for match in match_data:
        if match["Location"] == location:
            print(match)
def list_matches_by_time(time):
    for match in match_data:
        if match["Timing"] == time:
            print(match)

print("1. List of all the matches of a Team")
print("2. List of Matches on a Location")
print("3. List of Matches based on timing")
print("4. Exit")

x=int(input())

if x==1:
    team_name = input("Enter Team name: ")
    if team_name == "India" or team_name == "England"or team_name == "Australia":
        list_matches_by_teama(team_name)
    else:
        list_matches_by_teamb(team_name)
elif x==2:
    location= input("Enter Location: ")
    list_matches_by_location(location)
elif x==3:
    time= input("Enter time:")
    list_matches_by_time(time)
else:
    print("Invalid option")    