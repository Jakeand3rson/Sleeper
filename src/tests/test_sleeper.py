# -*- coding: utf-8 -*-
import pytest
import os


def test_get_token():
    """Make sure we are indeed getting a token"""
    """This is assuming you have a slack token in your environmental variables"""
    slack_token = os.getenv('SLACK_TOKEN')
    assert slack_token is not None
