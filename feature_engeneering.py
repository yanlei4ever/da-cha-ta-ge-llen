import numpy as np
from datetime import datetime
from workalendar.europe import France

# ass_assignment
names = [u'Crises', u'CMS', u'Domicile', u'Gestion', u'Gestion - Accueil Telephonique',
         u'Gestion Assurances', u'Gestion Clients', u'Gestion DZ', u'Gestion Relation Clienteles',
         u'Gestion Renault', u'Japon', u'Manager', u'M\xe9canicien', u'M\xe9dical', u'Nuit',
         u'Prestataires', u'RENAULT', u'RTC', u'Regulation Medicale', u'SAP', u'Services',
         u'Tech. Axa', u'Tech. Inter', u'Tech. Total', u'T\xe9l\xe9phonie']

name_encoder = dict(zip(names, [list(x) for x in np.eye(len(names))[:, 1:]]))

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# features
features = (['YEAR', 'MONTH', 'DAY', 'WEEKEND', 'HOLIDAY', 'TIMESLOT', 'DAYSLOT'] +
            weekdays[:-1] + names[1:] + ['CALLS'])

# French calendar object
calendar = France()

# first and last dates possibly considered
first = datetime.strptime('2011-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
last = datetime.strptime('2013-12-31 23:30:00', '%Y-%m-%d %H:%M:%S')


def parse_date(datestring):
    """ Parse date string and return relevant features. """

    # datetime object encoding data information
    date = datetime.strptime(datestring[:-4], '%Y-%m-%d %H:%M:%S')

    # create date-related predictor

    weekday = [0]*6
    if date.weekday() < 6:
        weekday[date.weekday()] = 1
    isweekend = int(weekday >= 5)
    isholiday = int(calendar.is_working_day(date.date()))

    timeslot = int((date - first).total_seconds() / 1800)  # number of half-hours since 01/01/2011 00:00
    dayslot = 2 * date.hour + date.minute / 30  # number of half-hours since midnight

    return [date.year, date.month, date.day,
            isweekend, isholiday, timeslot, dayslot] + weekday


def include_features(inputfile, outputfile):
    """ Include new features to cleaned table. """

    output = open(outputfile, 'w')
    output.write(';'.join(features) + '\n')  # header

    with open(inputfile, 'r') as data:
        data.readline()

        for line in data:
            date, name, calls = line.split(';')
            datefeatures = ';'.join([str(x) for x in parse_date(date)])
            namefeatures = name_encoder[name]

            output.write(';'.join(datefeatures + namefeatures + list(calls)))


if __name__ == '__main__':
    inputfile = '../data/clean/clean1.csv'
    outputfile = '../data/final/final1.csv'
    include_features(inputfile, outputfile)
