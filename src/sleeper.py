# -*- coding: utf-8 -*-

from slacker import Slacker
import os
import io
import csv
from time import sleep
from email.utils import formatdate

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
        sleep(1)
    return status_dict


def write_data(data):
    src_dir = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.join(src_dir, '..')
    file_path = os.path.join(project_root, 'status_data.txt')
    timestamp = formatdate()
    entry_dict = {'entry': {timestamp: data}}
    with io.open(file_path, 'a') as fh:
        writer = csv.DictWriter(fh, entry_dict.keys())
        writer.writerow(entry_dict)


if __name__ == '__main__':
    write_data(get_the_members())
