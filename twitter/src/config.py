"""
@date:   November 17, 2016
@author: Lior Bialik
"""

import argparse

options = None

def assertOptionsInit():
    assert options is not None, "options not initialized yet"


def getCmdLineOptions():
    parser = argparse.ArgumentParser(description='Twitter Statuses Fetcher')

    parser.add_argument('-n', '--screenName', required=True,
                        help='The screen name of the person you want to fetch')
    parser.add_argument('-t', '--tweetsToFetch', default=50, type=int,
                        help='The amount of tweets you want to fetch. If left empty the default is 50')

    cmdLineOptions = parser.parse_args()

    return cmdLineOptions


def getScreenName():
    assertOptionsInit()
    return options.screenName

def getTweetsToFetch():
    assertOptionsInit()
    return options.tweetsToFetch
