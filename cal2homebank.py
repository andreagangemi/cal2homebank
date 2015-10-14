__author__ = 'Andrea Gangemi'
__version__ = '0.0'

import re
import ConfigParser
from optparse import OptionParser

import urllib2  # the lib that handles the url stuff

ini_file_name = "settings.ini"


def extract_calendar_data(src):
    if 'http://' in src or 'https://' in src:
        data = urllib2.urlopen(src)  # it's a file like object and works just like a file
    else:
        data = open(src, 'r')
    for line in data:  # files are iterable
        print line

    return data


def main():

    calendar_src = ''

    usage = "usage: %prog [options] root_directory"
    parser = OptionParser(usage)
    parser.add_option("-v", "--verbose",
                      action="store_true",
                      dest="verbose",
                      default=True,
                      help="verbose mode ON [default]")

    (options, args) = parser.parse_args()

    try:
        config = ConfigParser.ConfigParser()
        config.read(ini_file_name)

        calendar_src = config.get('calendar', 'calendar_url')
    except ValueError, Argument:
        print 'Connect value: ' + Argument
        raw_input('press enter to continue')
    except:
        print 'Error reading ini file, using defaults'
        raw_input('press enter to continue')

    (options, args) = parser.parse_args()
    if len(args) == 0 and calendar_src == '':
        parser.error("incorrect number of arguments")

    if calendar_src == '':
        calendar_src = args[0]
    if options.verbose:
        print ' '
        print ' Hi, this is cal2homebank ' + __version__ + ' 8-)'
        print ' By Andrea Gangemi: http://harzack.flavors.me '
        print ' '
        print ' REMEMBER: cal2homebank COMES WITHOUT WARRANTY OF ANY KIND '
        print ' '
        print ' trying to extract expense from: ' + calendar_src


    data = extract_calendar_data(calendar_src)


if __name__ == "__main__":
    main()