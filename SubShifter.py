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
def replace(match):
    match = match.group()

    time = dt.datetime.strptime(match, '%H:%M:%S')

    if time.minute >= 12:
        time -= dt.timedelta(hours=0, minutes=1, seconds=30)  # 90 sec == 1 min + 30 sec:-)
        time.strftime('%H:%M:%S')

    return time.strftime('%H:%M:%S')


# Open Subtitle from Input path
with open(args['input'], 'r') as myFile:
    subtitle = myFile.read()

# timePattern is something like this:
#  00:00:00 --> H:M:S
timePattern = r'(\d+:\d+:\d+)'

# Shift Subtitle by use of replace() function rules
ret = re.sub(timePattern, replace, subtitle)

# Save shifted subtitle to Output path
with open(args['output'], 'w') as text_file:
    text_file.write(ret)
print('Done!')
