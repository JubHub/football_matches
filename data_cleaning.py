# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:51:55 2020

@author: jubin
"""


import pandas as pd

df = pd.read_csv("spi_matches.csv", sep = ",")

#Change date to a date format

df['date'] = pd.to_datetime(df['date']).dt.date

#Remove importance columns

df = df.drop(['importance1', 'importance2'], 1)

df = df.dropna()

df.to_csv('football_matches.csv', index = False)
