import sys
import os

script_dir = os.path.dirname(__file__)  # takes the currentfiles directory's name
mymodule_dir = os.path.join(script_dir, '..', 'include', 'class_curr')  # takes scrip_dir and goes back a directory and then takes the directory for the module
sys.path.append( mymodule_dir ) # adds specific path to interpreters search for modules

import currency as myModule # imports currency module as myModule

# for this project, I want to make a currency-converter that will convert currencies back
# and forth between different countries currencies

current = myModule.Currc()
current.load_csv("WS_XRU_D_csv_row 3.csv")

def main():
    current.find_exchange_rates("BHD", "BHD", "8/23/21", "3")

    print('These are the corresponding currencies with the country names:')
    print('#################################')
    for i, val in enumerate(current.countrynames):
        print(f'{i}) {val:<23}\t', end='')
        print(f'{current.countryCurr[i]:<4}#')
    #print(f'{current.countrynames}\t')
    #print(f'{current.countryCurr}')
    print('#################################')
    print(f"You can find the exchange rate on any day from today to last year, this is from {current.recentExch[len(current.recentExch) - 1]} to {current.recentExch[0]}")
    current.country1 = input("Please enter the 3 character currency abbreviation for the money that the currency is in:")
    amount = input("please enter the amount of money to be converted in terms of the previous currency:")
    current.country2 = input("please enter the 3 character for the currency abbreviation that the money should be converted to:")
    current.find_exchange_rates(current.country1, current.country2, "2/20/22", amount)



main()