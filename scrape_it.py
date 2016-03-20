import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


login_email = os.getenv("SLACK_EMAIL")
login_password = os.getenv("SLACK_PASSWORD")


urls = {
    'login': 'https://codefellows.slack.com/',
    '401': 'https://codefellows.slack.com/messages/sea-python-401d2/details/',
}


def get_page_source_via_selenium():
    """Use Firefox via Selenium to get page source."""
    # Initialize browser
    browser = webdriver.Firefox()

    # Go to the login page
    browser.get(urls['login'])

    # Get login fields and stuff in login credentials
    email_field = browser.find_element_by_id("email")
    password_field = browser.find_element_by_id("password")
    email_field.send_keys(login_email)
    password_field.send_keys(login_password, Keys.RETURN)

    # Go to details page now that we're authenticated
    browser.get(urls['401'])

    # Get that source, baby!
    html_source = browser.page_source

    browser.close()
    return html_source


def parse_data():
    source_string = get_page_source_via_selenium()
    soup = BeautifulSoup(source_string, 'html.parser')

    # Now do the work of actually parsing the data...


if __name__ == '__main__':
    pass
