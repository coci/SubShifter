import argparse
import re
import datetime as dt

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input subtitle")
ap.add_argument("-o", "--output", required=True, help="Path to output subtitle")
args = vars(ap.parse_args())


# this is where All the magic happens!
# we add -90 sec to subtitle time from the 12th minute to end of the subtitle
def replace(match, shiftPoint, shiftTime, shiftDitrction):

    time = dt.datetime.strptime(match, '%H:%M:%S')
    if all([time.hour >= shiftPoint.hour, time.minute >= shiftPoint.minute, time.second >= shiftPoint.second]):
        if shiftDitrction == '-':
            time -= dt.timedelta(hours=shiftTime.hour, minutes=shiftTime.minute,
                                 seconds=shiftTime.second)
        if shiftDitrction == '+':
            time += dt.timedelta(hours=shiftTime.hour, minutes=shiftTime.minute,
                                 seconds=shiftTime.second)

    return time.strftime('%H:%M:%S')


def getInputTimes():
    # Get start point of shift time from user:
    while True:
        try:
            shiftPoint = dt.datetime.strptime(
                input('Specify start point of shift in HH:MM:SS format: '), "%H:%M:%S")
            print(shiftPoint.strftime("%H:%M:%S"))
            break
        except ValueError:
            print("Please enter correct time in HH:MM:SS format\n")
    # Get shift time delta from user:
    while True:
        try:
            shiftTime = dt.datetime.strptime(
                input('Specify shift time in HH:MM:SS format: '), "%H:%M:%S")
            print(shiftTime.strftime("%H:%M:%S"))
            break
        except ValueError:
            print("Please enter correct time in HH:MM:SS format\n")

    # shift forward or delay?
    negative = {'-', '--', ''}
    positive = {'+', '++'}

    while True:
        choice = input('Delay - or + ? defult is - [-/+]: ')
        if choice in negative:

            shiftDitrction = '-'
            print('delay: - <--')
            break
        elif choice in positive:

            shiftDitrction = '+'
            print('delay: + -->')
            break
        else:
            print("Please respond with '+' or '-'")
    return shiftPoint, shiftTime, shiftDitrction


def main():
    # Open Subtitle from Input path
    with open(args['input'], 'r') as myFile:
        subtitle = myFile.read()

    # Get shiftPoint and ShiftTime from user
    shiftPoint, shiftTime, shiftDitrction = getInputTimes()
    # timePattern is something like this:
    #  00:00:00 --> H:M:S
    timePattern = r'(\d+:\d+:\d+)'

    # Shift Subtitle by use of replace() function rules
    ret = re.sub(timePattern, lambda m: replace(
        m.group(), shiftPoint, shiftTime, shiftDitrction), subtitle)

    # Save shifted subtitle to Output path
    with open(args['output'], 'w') as text_file:
        text_file.write(ret)
    print('Done!')


if __name__ == '__main__':
    main()
