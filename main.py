import pandas as pd
import numpy as np

emissions_csv = pd.read_csv('co2_emission.csv')
emissions = pd.DataFrame(emissions_csv)

emissions.columns = ['Country', 'Code', 'Year', 'Co2']
del emissions['Code']


norway_emission = emissions[(emissions['Country'] == 'Norway') & (emissions['Year'] > 2000)]

print(norway_emission.head())
# print(emissions.tail())
# print(emissions.shape)
# print(emissions.dtypes)
# print(emissions.describe())


