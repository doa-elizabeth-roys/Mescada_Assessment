leapYearsList = [] 

def is_leapYear(curent_year):
    if curent_year % 4 == 0:        #eg: 2020
        leapYearsList.append(curent_year + 4)
        for i in range(20):
            next_leap = leapYearsList[i] + 4
            leapYearsList.append(next_leap)
            

    elif curent_year % 4 == 1:      #eg: 2021
        leapYearsList.append(curent_year + 3)
        for i in range(20):
            next_leap = leapYearsList[i] + 4
            leapYearsList.append(next_leap)

    elif curent_year % 4 == 2:      #eg: 2022
        leapYearsList.append(curent_year + 2)
        for i in range(20):
            next_leap = leapYearsList[i] + 4
            leapYearsList.append(next_leap)

    elif curent_year % 4 == 3:      #eg: 2023
        leapYearsList.append(curent_year + 1)
        for i in range(20):
            next_leap = leapYearsList[i] + 4
            leapYearsList.append(next_leap)

    return leapYearsList



try:
    year = int(input("Enter current year: "))
    result = is_leapYear(year)
    print(f"The next 20 lear years are:{result}")
except ValueError:
    print("Invalid input")