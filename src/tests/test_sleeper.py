# -*- coding: utf-8 -*-
import pytest
import sleeper


@pytest.fixture(scope='session')
def correct_login():
    '''create correct login info'''
    return os.getenv('SLACK_TOKEN')
