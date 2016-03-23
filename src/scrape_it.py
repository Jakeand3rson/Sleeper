import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


login_email = os.getenv("SLACK_EMAIL")
login_password = os.getenv("SLACK_PASSWORD")


urls = {
    'login': 'https://codefellows.slack.com/',
    '401': 'https://codefellows.slack.com/messages/sea-python-401d2/details/',
}


def get_page_source_via_selenium():
    """Use Firefox via Selenium to get page source."""
    # Initialize browser
    print("Starting Firefox...")
    browser = webdriver.Firefox()
    print("Firefox started.")

    # Go to the login page
    print("Going to login page...")
    browser.get(urls['login'])
    print("At login page.")

    # Get login fields and stuff in login credentials
    # There's a weird bug here where the first attempt to find an element
    # fails, but subsequent attempts go through just fine.
    try:
        print("Making first attempt to find email field (should fail)...")
        email_field = browser.find_element_by_id("email")
        print("Attempt made - woah, it worked on the first try?")
    except:
        print("Making second attempt to find email field...")
        email_field = browser.find_element_by_id("email")
        print("Attempt made.")

    print("Making attempt to find password field...")
    password_field = browser.find_element_by_id("password")
    print("Attempt made.")

    print("Inputting login email...")
    email_field.send_keys(login_email)
    print("Login email input.")

    print("Inputting login password...")
    password_field.send_keys(login_password)
    print("Login password input.")

    print("Pressing enter...")
    password_field.send_keys(Keys.RETURN)
    print("Enter key pressed.")

    # The browser will wait until a page is loaded to process the next command
    # if the browser used .get() to navigate to the page. Here, since we're
    # just clicking a button, the browser won't wait on its own so we should
    # make sure that it's doing so so that our credentials will have actually
    # gone through.
    sleep_time = 10

    print("Sleeping for {} seconds...".format(sleep_time))
    sleep(sleep_time)
    print("Done sleeping.")

    # Go to details page now that we're authenticated
    print("Navigating to details page...")
    browser.get(urls['401'])
    print("Navigation complete.")

    # Click on the members list to open it
    # We've gotta feal with that weird bug again.
    try:
        print("Making first attempt to find member_count_title field " +
              "(should fail)...")
        member_count_field = browser.find_element_by_id("member_count_title")
        print("Attempt made - woah, this worked on the first try?")
    except:
        print("Making second attempt to find member_count_title field...")
        member_count_field = browser.find_element_by_id("member_count_title")
        print("Attempt made.")

    print("Clicking on the member count title field...")
    member_count_field.click()
    print("Clicked!")

    sleep_time = 2

    print("sleeping for {} seconds...".format(sleep_time))
    sleep(sleep_time)
    print("Done sleeping.")

    # Get that source, baby!
    print("Getting page source...")
    html_source = browser.page_source
    print("Source obtained.")

    sleep_time = 2

    print("Sleeping for {} seconds...".format(sleep_time))
    sleep(sleep_time)
    print("Done sleeping.")

    print("Closing browser...")
    browser.close()
    print("Browser closed.")

    print("Returning the page's source...")
    return html_source


def make_soup(page_source):
    return BeautifulSoup(page_source, 'parser.html')


def get_member_rows(souped_source):
    return souped_source.find_all('div', 'channel_page_member_row')


def main():
    if not (os.getenv("SLACK_EMAIL") and os.getenv("SLACK_PASSWORD")):
        raise LookupError(
            "Either or both of the environment variables 'SLACK_EMAIL' "
            "or 'SLACK_PASSWORD' are empty."
            "\n\n"
            "Don't be a shit in my cut.\n"
        )
    page_source = get_page_source_via_selenium()
    soup = make_soup(page_source)
    member_rows = get_member_rows(soup)
    print(member_rows)


if __name__ == '__main__':
    main()
