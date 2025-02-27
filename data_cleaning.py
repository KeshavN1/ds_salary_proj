# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:29:42 2025

@author: DELL
"""
import pandas as pd
df = pd.read_csv('ds_salaries.csv')

df = df[df['salary']!= '-1']