# -*- coding: utf-8 -*-

"""
This utility script exists to convert data from our initial crappy format
into something more useable, and then write it into the database.

OLD FORMAT (this was writted out to a file):
{'timestamp': {'slack_id_0': 'presence_0', 'slack_id_1': 'presence_1', ... }}

NEW FORMAT:
Save to DB as model, where fields = ['timestamp', 'slack_id', 'active']. There
will be many rows with identical timestamps.
"""
