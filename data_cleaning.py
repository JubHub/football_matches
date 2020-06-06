# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:51:55 2020

@author: jubin
"""


import pandas as pd

df = pd.read_csv("spi_matches.csv", sep = ",")

print(df.head())

print(df.describe())

