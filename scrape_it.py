from bs4 import BeautifulSoup
import urllib2


def pull_data():
    # This will pull data from the website
    openurl = urllib2.urlopen("https://codefellows.slack.com/messages/sea-python-401d2/details/")
    soup = BeautifulSoup(openurl)


def parse_data():
    # potential parsing of the data..
    pass


if __name__ == '__main__':
    pass
