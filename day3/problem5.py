# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.



def check_season(month):
    if month.lower()=="june" or  month.lower()=="july" or month.lower()=="augest": 
        return "summer"
    elif month.lower()=="february" or month.lower()=="january" or month.lower()=="december":
        return "winter"
    elif month.lower()=="april" or month.lower()=="may" or month.lower()=="march":
        return "Spring"
    else: return "Valid Input"
print(check_season("june"))