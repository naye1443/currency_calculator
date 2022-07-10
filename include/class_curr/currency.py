import csv

class Currc:

    def __init__(self):
        self.country1 = 1   # first countries currency
        self.country2 = 1   # second countries currency
        self.countrynames = []  # countries full name
        self.countryCurr = []   # countries currency
        self.recentExch = []    # dates of exchanges for up to a year
        self.countryexch = []   # each countries exchange rate

    def load_csv(self, name):
        if name[len(name) - 4:] != ".csv":
            name = name + ".csv"

        curfile = open( "rsrc/"+ name, "r")
        current = curfile.readlines()

        # now time to organize the information into

        #################################### saving country names ######################################################
        tempstr = current[1]
        tempstr = tempstr[14:] + ","    # adds a comma to end of string so that last country will be considered
        tempstr = tempstr.replace('\n', "") # gets ride of new line character for the string

        # needs to loop from comma to comma, then remove comma and and next 3 values
        i = 0
        previnc = 0
        while i < len(tempstr):
            if tempstr[i] == ',':   # when comes across a comma, set the previous index, and loop through current word behind the comma
                newstr = ""
                y = previnc
                while (y < i):  # takes word and puts into new string
                    newstr += tempstr[y]
                    y += 1
                if y != 0 and i != 0:   # if at the first comma, then dont put newstr in the countrynames list
                    self.countrynames.append(newstr)
                i += 4  # skip over the usless 4 characters in csv data
                previnc = i # previous index becomes where the current I is
            i += 1

        ############################## saving country currency name ####################################################

        tempstr = current[2]
        tempstr = tempstr[8:] + ","  # adds a comma to end of string so that last country will be considered
        tempstr = tempstr.replace('\n', "")  # gets ride of new line character for the string

        # needs to loop from comma to comma, then remove comma and and next 3 values
        i = 0
        previnc = 0
        while i < len(tempstr):
            if tempstr[i] == ',':   # when comes across a comma, set the previous index, and loop through current word behind the comma
                newstr = ""
                y = previnc + 1     # plus 1 gets rid of the comma
                while (y < i and y < previnc + 4 ):  # takes word and puts into new string
                    newstr += tempstr[y]
                    y += 1
                if y != 0 and i != 0:   # if at the first comma, then dont put newstr in the countrynames list
                    self.countryCurr.append(newstr)
                #i += 4  # skip over the usless 4 characters in csv data
                previnc = i # previous index becomes where the current I is
            i += 1

        ####################################### saves the date of currencies from 365 days ago(year) and gets their exchange rate ###################
        currlen = len(current) - 1
        commaYet = False
        z = 0
        previnc2 = 0
        templist = []
        for i in range(currlen,currlen - 365,-1):   # goes from latest record to a year ago
            commaYet = False
            # need to determine how long the date is
            currdate = ""
            y = 0
            previnc = 0
            while not commaYet:
                if current[i][y+1] == ',' :   # if the next value is a comma, set commaYet to true to end next loop
                    commaYet = True
                currdate += current[i][y]   # concatonate current value onto the current date
                y += 1
            self.recentExch.append(currdate) # append each date onto list of recent dates

            #### This is for exchange rates, do the same with the commas and store in a list
            templen = len(current[i]) - 1   # gets current length of current str
            for x in range(templen):    # loops through range of current str
                current[i] = current[i] + "\n"
                if current[i][x] == ',' or x == templen - 1:
                    newstr = ""
                    z = previnc2
                    while(z < x):
                        newstr += current[i][z]
                        z += 1
                    if z != 0 and i != 0:
                       templist.append(newstr)
                    previnc2 = x + 1
            self.countryexch.append(templist[:])  # appends a copy deep of the inner test list to testlist so that intestlist can be cleared
            templist.clear()
            previnc2 = 0;
            i += 1

    def find_exchange_rates(self, country1, country2, date, value):    # this function finds the exchange rates in terms of country1 & country2, and the date

        # first find the dates that we would like to use the exchange rates
        # just loop through the recentExch list until finding matching date, then take index value
        for i, val in enumerate(self.recentExch):
            if date == val:
                break

        ctryExch = self.countryexch[i]  # this gets the exact list at the correct date

        Country1Iter = 0
        Country2Iter = 0
        for i, val in enumerate(self.countryCurr):  # sets the location for in the list where the related exchange rate is held
            if country1 == val: # We are adding one because the layout of the list ctryExch includes the date as the first index. Add 1 to offset this
                Country1Iter = i + 1
                if country2 == val:
                    Country2Iter = Country1Iter
            elif country2 == val:
                Country2Iter = i + 1
                if country1 == val:
                    Country1Iter = Country2Iter


        # need to determine if the exchange rate can even be calulated. If values for country is '' or 'NaN', then the exchange rate could not be found

        if (ctryExch[Country1Iter] == '' or ctryExch[Country1Iter] == 'NaN'):
            print(f"There is not a valid entry for {country1}")
        elif (ctryExch[Country2Iter] == '' or ctryExch[Country2Iter] == 'NaN'):
            print(f"There is not a valid entry for {country2}")
        else:
            # next will create a current_Currc object that will be created and destroyed upon the finding of the exchange rates
            curr_curr = current_Currc(ctryExch, date, country1, country2, Country1Iter, Country2Iter)
            print(f'There are {curr_curr.conversion(value)} {country2} in {country1}')




class current_Currc:    # this class will be called for temporary exchange rate conversion

    def __init__(self, ctryExch, date, country1, country2, Country1Iter, Country2Iter):
        self.ctryExch = ctryExch
        self.date = date
        self.country1 = country1
        self.country2 = country2
        self.Country1Iter = Country1Iter
        self.Country2Iter = Country2Iter

    def conversion(self, value):    # convert the value in to the correct value
        exchangerate1 = self.ctryExch[self.Country1Iter]
        exchangerate2 = self.ctryExch[self.Country2Iter]

        # find the exchnage rate by dividing first given countries exchange rate in terms of USD and divide wanted
        # countries currency
        currExchRate = float(exchangerate2) / float(exchangerate1)   # this is exchange rate of how much of the first currency it would take to get second currency

        # to convert current money to new currency (currecurrency * (wantedcurrency/currcurrency))
        return float(value) * currExchRate # return the current conversion
