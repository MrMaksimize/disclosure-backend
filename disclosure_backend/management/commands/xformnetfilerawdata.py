"""
Command to download and load California campaign finance data from Netfile.
"""

import pdb

import pandas as pd

from netfile.management.commands import downloadnetfilerawdata


class Command(downloadnetfilerawdata.Command):
    help = 'Download and load the netfile raw data into the clean database.'
    app_name = 'disclosure'

    def load(self):
        data = pd.read_csv(self.combined_csv_path)
        print(self.combined_csv_path)
        print("There are %d rows in %s" % (len(data), self.combined_csv_path))
        print("Use these keys to query data: ")
        print(data.keys())
        print("e.g. data['cand_NamL'].unique() shows: ")
        print(data['cand_NamL'].unique())
        pdb.set_trace()
