# Read submit file, call predict model for each line and write output to new file
import numpy as np

# output line format
output_line = "{datetime}\t{ass_assignment}\t{calls}\r\n"

def predict(datetime, ass_assignment):
    """ Final prediction method being called.
        Takes the datetime and ass_assignment and predicts the number of calls.
    """
    return 0


def submit(inputfile, outputfile):
    """ Read submission file and make prediction, saving output to new file. """

    with open(inputfile, 'r') as input, open(outputfile, 'w') as output:
        # copy heading to file
        output.write(input.readline())

        # read each line, predict, and output
        for line in input:
            datetime, ass_assignment, _ = line.split('\t')

            calls = predict(datetime, ass_assignment)

            output.write(output_line.format(datetime=datetime,
                                            ass_assignment=ass_assignment,
                                            calls=calls))

if __name__ == '__main__':
    inputfile = './submission.txt'
    outputfile = './output.txt'

    submit(inputfile, outputfile)
