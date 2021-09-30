import numpy as np
import pandas as pd
Bungee = pd.read_csv('main.csv')
Bungee.Year = pd.to_datetime(Bungee.Year, format = '%Y')
Bungee.set_index('Year', drop=True, inplace=True)
Bungee.drop(columns='Total', inplace=True)
Bungees = Bungee.resample('10AS').sum()
Bungees['Population'] = Bungee['Population'].resample('10AS').max()
Bungees
