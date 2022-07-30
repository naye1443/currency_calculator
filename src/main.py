import sys
import os
from datetime import date

script_dir = os.path.dirname(__file__)  # takes the currentfiles directory's name
mymodule_dir = os.path.join(script_dir, '..', 'include', 'class_curr')  # takes scrip_dir and goes back a directory and then takes the directory for the module
sys.path.append( mymodule_dir ) # adds specific path to interpreters search for modules

import currency as myModule # imports currency module as myModule

# for this project, I want to make a currency-converter that will convert currencies back
# and forth between different countries currencies

current = myModule.Currc()
current.load_csv("WS_XRU_D_csv_row 3.csv")

def main():
    #current.find_exchange_rates("BHD", "BHD", "8/23/21", "3")

    # determine weather time_valid is not valid or not. Do this by changing current time value into Datetime object
    time_valid(current.recentExch[len(current.recentExch) - 1], current.recentExch[0], '5/20/2022')

    continloop = True
    contminloop = True
    while(continloop):
        contminloop = True

        print('These are the corresponding currencies with the country names:')

        print('#################################')
        for i, val in enumerate(current.countrynames):
            print(f'{i}) {val:<23}\t', end='')
            print(f'{current.countryCurr[i]:<4}#')
        print('#################################')

        date = input(f"You can find the exchange rate on any day from today to last year, this is from {current.recentExch[len(current.recentExch) - 1]} to {current.recentExch[0]}. please add day that you would like to see the exchange rate in M/DD/YYYY.(ex.3/10/2022):")
        time_valid(current.recentExch[len(current.recentExch) - 1], current.recentExch[0], date)


        print('###################################################################################################')
        current.country1 = input("Please enter the 3 character currency abbreviation for the money that the currency is in:")
        print('###################################################################################################')
        amount = input("please enter the amount of money to be converted in terms of the previous currency:")
        print('###################################################################################################')
        current.country2 = input("please enter the 3 character for the currency abbreviation that the money should be converted to:")
        print('###################################################################################################')
        current.find_exchange_rates(current.country1, current.country2, date, amount)   # prints the currency of country 1 in terms of country 2

        while contminloop:
            print('###################################################################################################')
            yesOrNo = input("would you like to do another conversion(Y/N):");
            if yesOrNo == 'y' or yesOrNo == 'Y':
                continloop = True
                contminloop = False
            elif yesOrNo == 'n' or yesOrNo == 'N':
                continloop = False
                contminloop = False
            else:
                print('###################################################################################################')
                print("This is not a valid input, please try again")
                contminloop = True



# this function takes the time that the user has answered and converts it into datetime class. Then compared to determine correct range of dates entered
def time_valid(lowertime, uppertime, usertime):

    val = []
    # convert time string into datetime format
    val.append(timeTodatetime(usertime))
    val.append(timeTodatetime(lowertime))
    val.append(timeTodatetime(uppertime))
    return val


def timeTodatetime(time):

    slashcount = 0
    day = ''
    month = ''
    year = ''
    x = 0
    for i, val in enumerate(time):
        if val == '/':
            slashcount += 1

        if slashcount == 1 and val == '/':  ## record the value before the slash as the month
            tempstr = ""
            while x < i:
                tempstr += time[x]
                x += 1
            x += 1  # increment 1 to skip last slash
            tempstr.strip("/")  # strip any spaces that were in the month
            month = tempstr
        elif slashcount == 2 and val == '/':  ## record data before the second slash
            tempstr = ""
            while x < i:
                tempstr += time[x]
                x += 1
            x += 1
            tempstr.strip("/")  # strip any spaces that were in the day
            day = tempstr
        elif i == len(time) - 1:  # have reached the end of string
            tempstr = ""
            while x <= i:
                tempstr += time[x]
                x += 1
            tempstr.strip("/")  # strip any spaces that were in the year
            year = tempstr

    tempdate = date.today()
    tempDate + ""
    for i in range(2):
        tempDate = tempDate + tempdate[i]

    year

    if len(year) == 2:
        year

    print(f"day:{day}\tmonth:{month}\tyear:{year}")

    return date(int(year), int(month), int(day))



main()
# wanna use wxPython for my gui