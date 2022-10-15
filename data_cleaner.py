import pandas as pd
import numpy as np
# load datasets
constructors = pd.read_csv('data/constructors.csv')
drivers = pd.read_csv('data/drivers.csv')
races = pd.read_csv('data/races.csv')
results = pd.read_csv('data/results.csv')

# merge datasets
df = pd.merge(results, races[['raceId', 'year', 'name', 'round']], on= 'raceId', how= 'left')
df = pd.merge(df, drivers[['driverId', 'driverRef', 'nationality']], on='driverId', how='left')
df = pd.merge(df, constructors[['constructorId', 'name', 'nationality']], on='constructorId', how='left')

# drop columns
df.drop(['number', 'position', 'positionText', 'laps', 'fastestLap', 'statusId', 'resultId', 'raceId', 'driverId', 'constructorId'], axis=1, inplace=True)

# rename columns
df = df.rename(columns={'rank': 'fastest_lap_rank', 'name_x': 'gp_name',
                    'nationality_x': 'driver_nationality', 'name_y': 'constructor_name', 'nationality_y': 'constructor_nationality',
                   'fastestLapTime': 'fastest_lap_time', 'fastestLapSpeed': 'fastest_lap_speed', 'driverRef': 'driver', 'positionOrder': 'position_order'})

# rearrange columns
df = df[['year', 'gp_name', 'round', 'driver', 'constructor_name', 'grid', 'position_order', 'points', 'time', 'milliseconds', 'fastest_lap_rank', 'fastest_lap_time', 'fastest_lap_speed', 'driver_nationality', 'constructor_nationality']]

# drop 2019 and results newer than 2000
df = df[df['year'] >= 2000]
# df = df[df['year'] != 2019]

# sort values
df = df.sort_values(by=['year', 'round', 'position_order'], ascending=[False, True, True])

# replace \N values in time col
df.time.replace('\\N', np.nan, inplace=True)
df.milliseconds.replace('\\N', np.nan, inplace=True)
df.fastest_lap_time.replace('\\N', np.nan, inplace=True)
df.fastest_lap_speed.replace('\\N', np.nan, inplace=True)
df.fastest_lap_rank.replace('\\N', np.nan, inplace=True)

# change datatypes
df.fastest_lap_speed = df.fastest_lap_speed.astype(float)
df.fastest_lap_rank = df.fastest_lap_rank.astype(float)
df.milliseconds = df.milliseconds.astype(float)

# reset index
df.reset_index(drop=True, inplace=True)
