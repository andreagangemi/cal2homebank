__author__ = 'andrea'
__version__ = '0.0'

import regex


import urllib2  # the lib that handles the url stuff

target_url = 'https://www.google.com/calendar/ical/t4a74d43tjj1vklmv9m435iv3o%40group.calendar.google.com/private-29effcce6007844db3cd1d795a2f3d81/basic.ics'

data = urllib2.urlopen(target_url)  # it's a file like object and works just like a file
for line in data:  # files are iterable
    print line
