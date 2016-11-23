import pandas as pd

# global variables
local_path = '/home/lucianodp/m2-data-science/methods-big-data-analytics/challenge-AXA/'
ass_assignments_to_remove = ['Evenements', 'Gestion Amex']


def remove_and_aggregate(inputfile, outputfile):
    """ Removes all columns except for predictors and computes total number of calls. """

    # read table into memory
    data = pd.read_csv(inputfile, sep=';', encoding='utf8',
                       usecols=['DATE', 'ASS_ASSIGNMENT', 'CSPL_RECEIVED_CALLS'])
    print 'Finished reading!'

    assert(data.notnull().values.any()), 'There are missing values!'

    # remove useless ass_assignments
    data = data[~data['ASS_ASSIGNMENT'].isin(ass_assignments_to_remove)]

    # aggregate on date,ass_assignment pairs and compute total number of calls
    aggregated = data.groupby(['DATE', 'ASS_ASSIGNMENT']).sum().reset_index()
    print 'Finished aggregation!'

    # output result to file
    aggregated.rename(inplace=True, columns={'ASS_ASSIGNMENT': 'NAME', 'CSPL_RECEIVED_CALLS': 'CALLS'})
    aggregated.to_csv(outputfile, sep=';', mode='w', encoding='utf8', index=False)
    print 'Written to file!'


if __name__ == '__main__':
    inputfile = local_path + 'data/raw/train_2011_2012_2013.csv'
    outputfile = local_path + 'data/clean/clean1.csv'
    remove_and_aggregate(inputfile, outputfile)