from bs4 import BeautifulSoup
# import urllib2
import urllib.request as req
from loginform import fill_login_form
import os


login_email = os.getenv("SLACK_EMAIL")
login_password = os.getenv("SLACK_PASSWORD")


urls = {
    'login': 'https://codefellows.slack.com/',
    '401': 'https://codefellows.slack.com/messages/sea-python-401d2/details/',
}


def get_login_page():
    login_page = req.urlopen(urls['login'])
    login_soup = BeautifulSoup(login_page, 'html.parser')
    login_text = BeautifulSoup.prettify(login_soup)
    return login_text


def do_login():
    login_text = get_login_page()
    login_response = fill_login_form(
        urls['login'],
        login_text,
        login_email,
        login_password,
    )
    return login_response


def pull_data():
    # This will pull data from the website
    # # openurl = urllib2.urlopen(
    #     "https://codefellows.slack.com/messages/sea-python-401d2/details/"
    # )
    openurl = req.urlopen(
        "https://codefellows.slack.com/messages/sea-python-401d2/details/"
    )
    soup = BeautifulSoup(openurl, 'html.parser')
    soup


def parse_data():
    # potential parsing of the data..
    pass


if __name__ == '__main__':
    pass
