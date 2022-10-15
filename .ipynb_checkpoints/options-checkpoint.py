import pandas as pd

# Preparing options for dropdowns

drivers = pd.read_csv("data/drivers.csv")
drivers_df = drivers[drivers.columns[1:2]]
drivers_to_dict = drivers_df.to_dict()
drivers_dict = drivers_to_dict['driverRef']
drivers_option = [{'label': str(x), 'value': y} for x, y in drivers_dict.items()]

constructors = pd.read_csv("data/constructors.csv")
constructors_df = constructors.get(['constructorId', 'name'])
constructors_to_dict = constructors_df.to_dict()
constructors_dict = constructors_to_dict['name']
constructors_option = [{'label': str(x), 'value': y} for x, y in constructors_dict.items()]


circuits = pd.read_csv("data/circuits.csv")
circuits_df = circuits.get(['circuitId', 'name'])
circuits_to_dict = circuits_df.to_dict()
circuits_dict = circuits_to_dict['name']
circuits_option = [{'label': str(x), 'value': y} for x, y in circuits_dict.items()]

status = pd.read_csv("data/status.csv")
status_df = status.get(['statusId', 'status'])
status_to_dict = status_df.to_dict()
status_dict = status_to_dict['status']
status_option = [{'label': str(x), 'value': y} for x, y in status_dict.items()]
