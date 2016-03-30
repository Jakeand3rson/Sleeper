# -*- coding: utf-8 -*-

from slacker import Slacker
import os
from time import sleep

channel_name = 'sea-python-401d2'


def get_token():
    return os.environ.get('SLACK_TOKEN')

s = Slacker(get_token())


def channel_id():
    return s.channels.get_channel_id(channel_name)


def channel_info():
    return s.channels.info(channel_id())


def get_the_members():
    members = channel_info().body['channel']['members']
    status_dict = {}
    for m in members:
        status_dict[m] = s.users.get_presence(m).body['presence']
        # Add a sleep call to avoid rate-limiting
        # sleep(1)
    return status_dict

print(get_the_members())
