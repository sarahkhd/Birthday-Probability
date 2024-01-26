import datetime, random

def getBirthdays(numberOfBirthdays):
    """returns a list of number random date objects for birthdays"""
    birthdays = []

    for i in range (numberOfBirthdays):
        # the year is unimportant for this simulation as long as all birthdays have the same year
        startOfYear = datetime.date(2003,1,1)

        #get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """"returns the date object of a birthday that occurs more than once in the birthdays list"""
    if len(birthdays) == len(set(birthdays)):
        return None # means all birthdays are unique so no return

    #compare each bday to every other bday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # return matching bday

#intro
print('''Birthday Probability shows us that in groups of N people, the odds that
 two of them have matching birthdays is surprisingly large. this program does a
 Monte Carlo simulation to explore this concept.''')

#setting up a tuple of months in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sept', 'Oct', ' Nov', 'Dec')

while True:
    print('How many birthdays should I generate? (max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break #only if user has entered valid amt
print()

#generate and display bdays
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # show a comma for each bday affter the first bday
        print(',', end='')
        monthName = MONTHS[birthday.month -1]
        dateText = '{} {}'. format(monthName, birthday.day)
        print(dateText, end='')
print()
print()

#determine if there are 2 bdays that match
match =getMatch(birthdays)

#display the results
print('In this simulation,', end='')
if match != None:
    monthName = MONTHS[match.month -1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

#run the 100,000 simulations
print('generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to Begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0 #shows how many sims had matching bdays in them
for i in range(100_000):
    #report the progress every 10,000 sims
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

#displaying sim results
probability = round(simMatch / 100_000 * 100, 2)
print('out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. this means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('that\'s probably more than you would think!')

