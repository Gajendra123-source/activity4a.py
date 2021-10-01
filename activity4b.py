# Jendra Poudel
# ISQA_3900-851, 09/25/2021
# This function output letter grade based on average of
# input scores out of 100


def main():
    # list of scores to store grade values and setting variable to 0.
    grades = []
    repeat = True
    total = 0
    counter = 0
    average = 0
    gradeLetter = ''
    # Repeat loop till user enters -1
    while repeat:

        try:
            value = int( input('Enter score : '))

            if value == -1:
                # set repeat to False to stop execution
                repeat = False
            else:
                # increment the counter by 1
                counter = counter + 1
                # add value to total
                total = total + value
                # add value to grades
                grades.append( value )
        except ValueError:
            print( 'Invalid input' )
    # calculate the average score
    average = total / counter
    # find the letter grade for average value
    if average >= 92.50 and average <= 100:
        gradeLetter = 'A'
    elif average >= 88.5 and average <= 92.49:
        gradeLetter = 'B+'
    elif average >= 82.50 and average <= 88.49:
        gradeLetter = 'B'
    elif average >= 77.5 and average <= 82.49:
        gradeLetter = 'C+'
    elif average >= 72.50 and average <= 77.49:
        gradeLetter = 'C'
    elif average >= 59.5 and average <= 72.49:
        gradeLetter = 'B'
    else:
        gradeLetter = 'F'
    # Print total score
    print('Total Score', total)
    # Print average
    print('Average', average)
    # Print gradeLetter
    print('Letter Grade', gradeLetter)


# main method
main()
