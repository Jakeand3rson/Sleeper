# -*- coding: utf-8 -*-
import pytest
import os
from .. sleeper import get_token, channel_id

channel_name = 'sea-python-401d2'


def test_get_token():
    """Make sure we are indeed getting a token"""
    """This is assuming you have a slack token in your environ variables"""
    slack_token = os.getenv('SLACK_TOKEN')
    assert get_token() == slack_token


def test_channel_id():
    """Make sure that the function that gets our channel id is working"""
    slack_token = os.getenv('SLACK_TOKEN')
    from slacker import Slacker
    s = Slacker(slack_token)
    assert channel_id() == s.channels.get_channel_id(channel_name)
