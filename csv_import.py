#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

import pandas as pd
import sys

filename = sys.argv[1]

export_filename = filename.removesuffix('.csv') + "_sage.csv"

df = pd.read_csv(filename)

print(df)

del df['Balance']

df['Date'] = pd.to_datetime(df.Date, format="%Y%m%d")

print (df)

df.to_csv(export_filename, index=False)