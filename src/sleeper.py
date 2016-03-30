# -*- coding: utf-8 -*-

from slacker import Slacker
import os
from time import sleep

channel_name = 'sea-python-401d2'


def get_token():
    return os.environ.get('SLACK_TOKEN')

s = Slacker(get_token())


channel_id = s.channels.get_channel_id(channel_name)
channel_info = s.channels.info(channel_id)
members = channel_info.body['channel']['members']

for m in members:
    print(m, s.users.get_presence(m).body['presence'])
    sleep(1)
