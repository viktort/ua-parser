"""
    Wrapper around the python lib - pass in a string or a file of user agent strings
    Run:
        # python main.py <inputFormat: string|file> <uaString|filePath> <delimiter: \t|,|json>
"""

__author__ = 'viktor.trako@holidayextras.com (Viktor Trako)'

from ua_parser import user_agent_parser
import sys
import json
# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)


def parseFromFile(filePath, delimiter):
    "Parse user agents using a file input"
    return filePath


def parseFromString(uaString, delimiter):
    "Parse user agents using a file input."
    return parseUaString(uaString, delimiter)


def parseUaString(str, delimiter):
    "Use the provided lib to parse the user agent string"
    # print 'UA String to Parse =', sys.argv[1]
    # On the server, you could use a WebOB request object.
    # user_agent_string = request.META.get('HTTP_USER_AGENT')

    # def main(argv):

    # For demonstration purposes, though an iPhone ...
    # user_agent_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
    user_agent_string = str
    # Get back a big dictionary of all the goodies.
    result_dict = user_agent_parser.Parse(user_agent_string)

    uaJson = json.dumps(result_dict, separators="," ":")

    # print json.dumps(result_dict['user_agent'], separators="," ":")
    # {'major': '5', 'minor': '1', 'family': 'Mobile Safari', 'patch': None}

    # print json.dumps(result_dict['os'], separators="," ":")
    # {'major': '5', 'patch_minor': None, 'minor': '1', 'family': 'iOS', 'patch': None}

    # print json.dumps(result_dict['device'], separators="," ":")
    # {'family': 'iPhone'}
    # print '__name__ = ', __name__
    if (delimiter == 'json'):
        return uaJson
    else:
        return "Unknown delimiter"

if len(sys.argv) == 4:
    inputType = sys.argv[1]
    inputFormat = sys.argv[2]
    delimiter = sys.argv[3]

    if inputType == 'string':
        parsedUaString = parseFromString(inputFormat, delimiter)
        print parsedUaString
    #     pass it to string parser
    if inputType == 'file':
        parseFromFile(inputFormat, delimiter)
    else:
        sys.exit(1)
else:
    print 'Usage: main.py <user agent string>'
    sys.exit(1)