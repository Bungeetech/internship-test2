import numpy as np
import pandas as pd
crime = pd.read_csv('main.csv')
crime.Year = pd.to_datetime(crime.Year, format = '%Y')
crime.set_index('Year', drop=True, inplace=True)
crime.drop(columns='Total', inplace=True)
crimes = crime.resample('10AS').sum()
crimes['Population'] = crime['Population'].resample('10AS').max()
crimes
