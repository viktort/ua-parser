from ua_parser import user_agent_parser
import sys
import json
# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

if len(sys.argv) == 2:
    # print 'UA String to Parse =', sys.argv[1]
    # On the server, you could use a WebOB request object.
    # user_agent_string = request.META.get('HTTP_USER_AGENT')

    # def main(argv):

    # For demonstration purposes, though an iPhone ...
    # user_agent_string = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'
    user_agent_string = sys.argv[1]
    # Get back a big dictionary of all the goodies.
    result_dict = user_agent_parser.Parse(user_agent_string)

    # print json.dumps(result_dict, separators="," ":")

    print json.dumps(result_dict['user_agent'], separators="," ":")
    # {'major': '5', 'minor': '1', 'family': 'Mobile Safari', 'patch': None}

    print json.dumps(result_dict['os'], separators="," ":")
    # {'major': '5', 'patch_minor': None, 'minor': '1', 'family': 'iOS', 'patch': None}

    print json.dumps(result_dict['device'], separators="," ":")
    # {'family': 'iPhone'}
    # print '__name__ = ', __name__
    sys.exit(0)
else:
    print 'Usage: main.py <user agent string>'
    sys.exit(1)

