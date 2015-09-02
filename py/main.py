"""
    Wrapper around the python lib - pass in a string or a file of user agent strings
    Run:
        # python main.py <inputFormat: string|file> <uaString|filePath> <delimiter: \t|,|json>
"""

__author__ = 'viktor.trako@holidayextras.com (Viktor Trako)'

import sys
import user_agent_wrapper
# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

if len(sys.argv) == 4:
    inputType = sys.argv[1]
    inputFormat = sys.argv[2]
    delimiter = sys.argv[3]

    if inputType == 'string':
        parsedUaString = user_agent_wrapper.parseFromString(inputFormat, delimiter)
        print parsedUaString
    #     pass it to string parser
    if inputType == 'file':
        user_agent_wrapper.parseFromFile(inputFormat, delimiter)
    else:
        sys.exit(1)
else:
    print 'Usage: main.py <user agent string>'
    sys.exit(1)
