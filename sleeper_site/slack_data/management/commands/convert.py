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

from django.core.management.base import BaseCommand

import io
import json
import pandas as pd
from sqlalchemy import create_engine


class Command(BaseCommand):

    def get_data(self, data_file):
        converted_dict = {}
        with io.open(data_file, 'r') as fh:
            for line in fh:
                jdata = json.loads(line)
                converted_dict.update(jdata)
        return converted_dict

    def dict_to_dataframe(self, input_dict):
        col_names = ['timestamp', 'slack_id', 'active']
        new_frame = pd.DataFrame([['', '', '']], columns=col_names)
        # counter = 0
        for outer_key, outer_val in input_dict.items():
            # if counter > 20:
            #     break
            # counter += 1
            for inner_key, inner_val in outer_val.items():
                if inner_val == 'active':
                    add_this = pd.DataFrame(
                        [[outer_key, inner_key, True]],
                        columns=col_names,
                    )
                else:
                    add_this = pd.DataFrame(
                        [[outer_key, inner_key, False]],
                        columns=col_names,
                    )
                new_frame = new_frame.append(add_this, ignore_index=True)
        new_frame = new_frame.drop([0])
        new_frame = new_frame.reindex()
        return new_frame

    def write_to_db(self, input_dataframe, db_url, db_table_name):
        engine = create_engine(db_url)
        input_dataframe.to_sql(
            db_table_name,
            engine,
            if_exists='append',
            index=False,
        )

    def handle(self, *args, **options):
        data_file = options['file']
        db_url = options['db_url']
        db_table_name = options['db_table_name']
        data_dict = self.get_data(data_file)
        frame = self.dict_to_dataframe(data_dict)
        self.write_to_db(frame, db_url, db_table_name)
