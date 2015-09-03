"""User Agent Wrapper unit tests

"""

__author__ = 'viktor.trako@holidayextras.com (Viktor Trako)'

import os
import re
import unittest
import yaml
import json
import user_agent_wrapper

TEST_RESOURCES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                  '../../test_resources')

class ParseStringWithGivenDelimiter(unittest.TestCase):
    def testUserAgentStringsFromFile(self):
        self.runParseUserAgentStringsFromFile()
        # self.runParseUserAgentStringsFromFile(os.path.join(
        #     TEST_RESOURCES_DIR, 'random_user_agent_strings.txt'))

    def testUserAgentStringFromString(self):
        self.runParserUserAgentStringFromStringAsJson()

    def runParserUserAgentStringFromStringAsJson(self):

        userAgentString = "Mozilla/5.0 (Linux; Android 4.2.2; GT-I9195 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Mobile Safari/537.36"
        delimiter = "json"

        expected = {
            "device":{
                "family":"Samsung GT-I9195"
            },
            "os":{
                "major":"4",
                "patch_minor": None,
                "minor":"2",
                "family":"Android",
                "patch":"2"
            },
            "user_agent":{
                "major":"44",
                "minor":"0",
                "family":"Chrome Mobile",
                "patch":"2403"
            },
            "string":"Mozilla/5.0 (Linux; Android 4.2.2; GT-I9195 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Mobile Safari/537.36"
        }

        result = json.loads(user_agent_wrapper.parseFromString(userAgentString, delimiter))
        device = expected['device']['family']
        os = expected['os']['family'];
        browser = expected['user_agent']['family'];
        string = expected['string'];

        self.assertEqual(device, result['device']['family'])
        self.assertEqual(os, result['os']['family'])
        self.assertEqual(browser, result['user_agent']['family'])
        self.assertEqual(string, result['string'])

    def runParseUserAgentStringsFromFile(self):
        userAgentString = "Mozilla/5.0 (Linux; Android 4.2.2; GT-I9195 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.133 Mobile Safari/537.36"
        delimiter = ","

        result = user_agent_wrapper.parseFromFile(userAgentString, delimiter)
        print result

if __name__ == '__main__':
    unittest.main()
