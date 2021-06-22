#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

import pandas as pd
import sys

filename = sys.argv[1]

export_filename = filename.removesuffix('.csv') + "_sage.csv"

df = pd.read_csv(filename, parse_dates=['Date'])

del df['Balance']

print(df)

df.to_csv(export_filename, index=False, line_terminator='\r\n', date_format="%d/%m/%Y")