#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 24 12:01:28 2025

@author: ridwan-ayinde

"""

# 🐼 Pandas = data table toolbox | head() = preview rows | info() = structure
# non-null = good value | Python starts counting from 0


import pandas as pd

# Load CSV file

df =  pd.read_csv ("/home/ridwan-ayinde/Desktop/MIT Emerging Talent/Data Engineering/nyc_taxi_sample.csv")

#print (df.head())

# print (df.info())


#df.describe() shows summary statistics — 25%, 50%, 
#75% are percentiles that help understand how your numbers are spread out.

#print (df.describe())

#Convert pickup and dropoff datetime

df['pickup_datetime'] = pd.to_datetime (df['pickup_datetime'], errors ='coerce')
df['dropoff_datetime'] = pd.to_datetime (df['dropoff_datetime'], errors = 'coerce' )

#Drop rows with mssing (NaN) values

df.dropna (inplace = True)

#Remove rows with negative fare

df = df [df['fare_amount'] > 0]

#Remove rows with zero or negative passengers

df = df[df['passenger_count'] > 0]

#Remove index after removing rows

df.reset_index(drop=True, inplace = True)

#View cleaned data

print (df.head())
print (df.info())

