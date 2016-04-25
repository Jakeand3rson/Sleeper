# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from slack_data.models import UserPresence

import os
from time import sleep
from datetime import datetime as dt
from slacker import Slacker


class Command(BaseCommand):

    def get_token(self):
        return os.environ.get('SLACK_TOKEN')

    def channel_id(self):
        return self.slacker.channels.get_channel_id(self.channel_name)

    def channel_info(self):
        return self.slacker.channels.info(self.channel_id())

    def get_the_members(self):
        members = self.channel_info().body['channel']['members']
        status_dict = {}
        for member in members:
            users = self.slacker.users
            status_dict[member] = users.get_presence(member).body['presence']
            sleep(1)  # Sleep call to avoid rate-limiting
        return status_dict

    def save_data(self, data):
        timestamp = dt.utcnow()
        for key, val in data.items():
            presence = UserPresence()
            presence.timestamp = timestamp
            presence.slack_id = key
            presence.active = True if val == 'active' else False
            presence.save()

    def handle(self, *args, **kwargs):
        self.channel_name = 'sea-python-401d2'
        self.slacker = Slacker(self.get_token())

        self.save_data(self.get_the_members())
