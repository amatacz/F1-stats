import pandas as pd
import pprint

circuits = pd.read_csv('data/circuits.csv')
constructor_results = pd.read_csv('data/constructor_results.csv')
constructor_standings = pd.read_csv('data/constructor_standings.csv')
constructors = pd.read_csv('data/constructors.csv')
drivers = pd.read_csv('data/drivers.csv')
lap_times = pd.read_csv('data/lap_times.csv')
pit_stops = pd.read_csv('data/pit_stops.csv')
qualifying = pd.read_csv('data/qualifying.csv')
races = pd.read_csv('data/races.csv')
seasons = pd.read_csv('data/seasons.csv')
sprint_results = pd.read_csv('data/sprint_results.csv')
status = pd.read_csv('data/status.csv')
results = pd.read_csv('data/results.csv')



# Processing data -> extracting data for seasons '00-22

races_df = pd.read_csv("data/races.csv")
races_df = races_df[races_df['year'] >= 2012].sort_values(by='year')

results_df = pd.read_csv("data/results.csv")
results_df = pd.merge(races_df, results_df, on=['raceId'])

#results_df.to_csv("data/processed.csv")


print(results_df.groupby('driverId'))

