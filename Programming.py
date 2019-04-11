def Years(Year):
    if Year%2000 == 0:
        return "Visokosniy"
    elif Year%400 == 0:
        return "Delete away"
    elif Year%4 == 0:
        return "Year " + str(Year) + " visokosniy"
    else:
        return "Delete C:/"

while True:
    print(Years(int(input("Year: "))))
    
